# Trained on handwritten_digit_classification.ipynb model

import streamlit as st
from streamlit_drawable_canvas import st_canvas
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import numpy as np

# Define the CNN architecture
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1,10, kernel_size=5)
        self.conv2 = nn.Conv2d(10,10, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fcl = nn.Linear(160,50)
        self.fcl2 = nn.Linear(50,10)
    
    def forward(self,x):
        x = F.relu(F.max_pool2d(self.conv1(x),2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)),2))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fcl(x))
        x = F.dropout(x, training=self.training)
        x = self.fcl2(x)
        return x

# Load trained model
device = torch.device('cpu')
model = CNN()
model.load_state_dict(torch.load("mnist_cnn_weights.pth", map_location=device))
model.eval()

st.title("🖌️ MNIST Handwritten Digit Recognizer")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="#000000",  # Black ink
    stroke_width=10,
    stroke_color="#FFFFFF",  # White digit
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):
    if canvas_result.image_data is not None:
        # Convert drawing to PIL image
        img = Image.fromarray((canvas_result.image_data[:, :, 0]).astype('uint8'))  # Grayscale
        img = img.resize((28, 28)).convert("L")  # Resize and convert to grayscale
        img = np.array(img)

        # Invert colors and normalize
        img = 255 - img
        img = img / 255.0

        # Convert to tensor
        tensor = torch.tensor(img, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # Shape: (1, 1, 28, 28)

        with torch.no_grad():
            output = model(tensor)
            pred = output.argmax(dim=1, keepdim=True).item()
        
        st.success(f"🧠 Predicted Digit: {pred}")
