# Trained on modelsimplified_MNIST.ipynb model

import streamlit as st
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import numpy as np
from streamlit_drawable_canvas import st_canvas

# Load your trained model
model = torch.load("mnist_cnn.pth", map_location=torch.device("cpu"), weights_only=False)
model.eval()


# Set up canvas
st.title("Draw a Digit (0-9) 🖌️")
st.markdown("Draw inside the box below. Then click **Predict**.")

canvas_result = st_canvas(
    fill_color="#000000",  # Black ink
    stroke_width=15,
    stroke_color="#FFFFFF",  # White background
    background_color="#000000",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas"
)

# When the canvas has image data
if canvas_result.image_data is not None:
    img = canvas_result.image_data

    if st.button("Predict"):
        # Preprocess: Resize to 28x28, grayscale, tensor
        image = Image.fromarray((img[:, :, 0]).astype('uint8'), mode='L')
        image = image.resize((28, 28))
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
        input_tensor = transform(image).unsqueeze(0) # type: ignore

        # Predict
        with torch.no_grad():
            output = model(input_tensor)
            pred = output.argmax(dim=1).item()
        
        st.image(image.resize((140, 140)), caption="Processed Image", use_column_width=False)
        st.subheader(f"Predicted Digit: **{pred}**")
