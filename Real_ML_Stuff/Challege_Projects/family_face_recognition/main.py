# main.py

import os
import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1
from sklearn.metrics.pairwise import cosine_similarity

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize MTCNN and FaceNet model
mtcnn = MTCNN(keep_all=True, device=device)
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)

KNOWN_FOLDER = r"./Known_faces"
THRESHOLD = 0.7

def extract_embedding(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return None
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = mtcnn(img_rgb)
    if faces is None:
        return None

    if isinstance(faces, torch.Tensor):
        # faces shape: [N, 3, 160, 160], take first face
        face_tensor = faces[0]
    elif isinstance(faces, list):
        face_tensor = faces[0]
    else:
        face_tensor = faces

    with torch.no_grad():
        embedding = model(face_tensor.unsqueeze(0).to(device))
    return embedding.cpu().numpy()



# Load known embeddings
known_embeddings = []
known_names = []

print("Loading known faces...")
for person_name in os.listdir(KNOWN_FOLDER):
    person_folder = os.path.join(KNOWN_FOLDER, person_name)
    if os.path.isdir(person_folder):
        for img_file in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_file)
            emb = extract_embedding(img_path)
            if emb is not None:
                known_embeddings.append(emb)
                known_names.append(person_name)
            else:
                print(f"Warning: Could not process image {img_path}")

if len(known_embeddings) == 0:
    print("No known faces found! Exiting.")
    exit()

known_embeddings = np.vstack(known_embeddings)
print(f"Loaded embeddings for {len(known_names)} images.")

# Start webcam
cap = cv2.VideoCapture(0)
print("Starting webcam... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = mtcnn(frame_rgb)

    if faces is not None:
        for i, face_tensor in enumerate(faces):
            with torch.no_grad():
                embedding = model(face_tensor.unsqueeze(0).to(device)).cpu().numpy()

            sims = cosine_similarity(embedding, known_embeddings)[0]
            best_idx = np.argmax(sims)
            best_score = sims[best_idx]

            name = known_names[best_idx] if best_score > THRESHOLD else "Unknown"

            # Get corresponding bounding box from mtcnn.detect()
            boxes, _ = mtcnn.detect(frame_rgb) # type: ignore
            if boxes is not None and len(boxes) > i:
                x1, y1, x2, y2 = boxes[i].astype(int)

                # Draw rectangle and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{name} ({best_score:.2f})"
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
