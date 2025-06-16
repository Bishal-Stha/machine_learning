import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from PIL import Image
import copy

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load and preprocess image
def load_image(path, max_size=512, shape=None):
    image = Image.open(path).convert("RGB")

    # Resize
    if max(image.size) > max_size:
        size = max_size
    else:
        size = max(image.size)

    if shape:
        size = shape  # (height, width)

    if isinstance(size, int):
        transform = transforms.Compose([
            transforms.Resize(size),
            transforms.ToTensor()
        ])
    else:
        transform = transforms.Compose([
            transforms.Resize(size),  # size is (height, width)
            transforms.ToTensor()
        ])

    image = transform(image).unsqueeze(0)  # Add batch dimension # type: ignore
    return image.to(device, torch.float)

# Convert tensor to PIL image
def tensor_to_image(tensor):
    image = tensor.cpu().clone().detach()
    image = image.squeeze(0)
    image = transforms.ToPILImage()(image)
    return image

# Content Loss
class ContentLoss(nn.Module):
    def __init__(self, target):
        super().__init__()
        self.target = target.detach()

    def forward(self, input):
        self.loss = nn.functional.mse_loss(input, self.target)
        return input

# Style Loss
class StyleLoss(nn.Module):
    def __init__(self, target_feature):
        super().__init__()
        self.target = self.gram_matrix(target_feature).detach()

    def gram_matrix(self, input):
        b, c, h, w = input.size()
        features = input.view(c, h * w)
        G = torch.mm(features, features.t())
        return G / (c * h * w)

    def forward(self, input):
        G = self.gram_matrix(input)
        self.loss = nn.functional.mse_loss(G, self.target)
        return input

# Model and losses
def get_style_model_and_losses(cnn, style_img, content_img,
                                style_layers=None, content_layers=None):
    if style_layers is None:
        style_layers = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']
    if content_layers is None:
        content_layers = ['conv_4']

    cnn = copy.deepcopy(cnn)

    model = nn.Sequential().to(device)
    content_losses = []
    style_losses = []

    i = 0
    for layer in cnn.children():
        if isinstance(layer, nn.Conv2d):
            i += 1
            name = f'conv_{i}'
        elif isinstance(layer, nn.ReLU):
            name = f'relu_{i}'
            layer = nn.ReLU(inplace=False)
        elif isinstance(layer, nn.MaxPool2d):
            name = f'pool_{i}'
        elif isinstance(layer, nn.BatchNorm2d):
            name = f'bn_{i}'
        else:
            continue

        model.add_module(name, layer)

        if name in content_layers:
            target = model(content_img).detach()
            content_loss = ContentLoss(target)
            model.add_module(f"content_loss_{i}", content_loss)
            content_losses.append(content_loss)

        if name in style_layers:
            target_feature = model(style_img).detach()
            style_loss = StyleLoss(target_feature)
            model.add_module(f"style_loss_{i}", style_loss)
            style_losses.append(style_loss)

    return model, style_losses, content_losses

# Style transfer function
def run_style_transfer(cnn, content_img, style_img, input_img, num_steps=300,
                       style_weight=1e6, content_weight=1):
    print("Building model...")
    model, style_losses, content_losses = get_style_model_and_losses(
        cnn, style_img, content_img)

    optimizer = optim.LBFGS([input_img.requires_grad_()])

    print("Starting style transfer...")
    run = [0]
    while run[0] <= num_steps:

        def closure():
            input_img.data.clamp_(0, 1)
            optimizer.zero_grad()
            model(input_img)
            style_score = sum(sl.loss for sl in style_losses)
            content_score = sum(cl.loss for cl in content_losses)
            loss = style_score * style_weight + content_score * content_weight
            loss.backward() # type: ignore

            run[0] += 1
            if run[0] % 50 == 0:
                print(f"Step {run[0]}:")
                print(f"  Style Loss: {style_score.item():.4f}") # type: ignore
                print(f"  Content Loss: {content_score.item():.4f}") # type: ignore

            return style_score + content_score

        optimizer.step(closure)

    input_img.data.clamp_(0, 1)
    return input_img

# Main execution
if __name__ == "__main__":
    content_path = "./bishalHero.JPG"
    style_path = "./filter2.jpeg"

    content_img = load_image(content_path)
    style_img = load_image(style_path, shape=(content_img.size(2), content_img.size(3)))
    input_img = content_img.clone()

    cnn = models.vgg19(pretrained=True).features.to(device).eval()

    output = run_style_transfer(cnn, content_img, style_img, input_img)

    result = tensor_to_image(output)
    result.save("filtered_bishal.jpg")
    result.show()
