# face_recognition_app.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from sklearn.metrics.pairwise import cosine_similarity
import tempfile
import pickle
import os

# Initialize models
mtcnn = MTCNN(image_size=160, margin=0, keep_all=False)
facenet = InceptionResnetV1(pretrained='vggface2').eval()

# Storage for embeddings
EMBEDDING_PATH = "known_faces.pkl"
if os.path.exists(EMBEDDING_PATH):
    with open(EMBEDDING_PATH, "rb") as f:
        known_faces = pickle.load(f)
else: 
    known_faces = {}

# Helper: Compare embeddings
def get_match_name(known_faces, input_embedding, threshold=0.7):
    for name, emb in known_faces.items():
        similarity = cosine_similarity([emb], [input_embedding])[0][0] # type: ignore
        if similarity > threshold:
            return name
    return "Unknown"

# App UI
st.title("🔍 Face Recognition App")
st.write("Upload a face image, give it a name, and use your webcam to recognize it.")

# Section 1: Add new known face
uploaded_file = st.file_uploader("Upload face image", type=["jpg", "jpeg", "png"])
person_name = st.text_input("Enter a name for this person")

if uploaded_file and person_name:
    img = Image.open(uploaded_file)
    face = mtcnn(img)
    if face is not None:
        embedding = facenet(face.unsqueeze(0)).detach().numpy()[0]
        known_faces[person_name] = embedding
        with open(EMBEDDING_PATH, "wb") as f:
            pickle.dump(known_faces, f)
        st.success(f"✅ {person_name} added to the database.")
    else:
        st.warning("No face detected in the image.")

# Section 2: Start webcam recognition
if st.button("Start Webcam Recognition"):
    cap = cv2.VideoCapture(0)
    FRAME_WINDOW = st.image([])

    st.info("Press 'Stop' button to exit webcam recognition.")
    stop_btn = st.button("Stop")

    while cap.isOpened() and not stop_btn:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(rgb_frame)

        face = mtcnn(img_pil)
        if face is not None:
            embedding = facenet(face.unsqueeze(0)).detach().numpy()[0]
            match = get_match_name(known_faces, embedding)
            cv2.putText(frame, match, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        FRAME_WINDOW.image(frame, channels="BGR")

    cap.release()
    st.success("Webcam stopped.")

# Optional: Display saved names
if st.checkbox("Show saved names"):
    st.write(list(known_faces.keys()))
