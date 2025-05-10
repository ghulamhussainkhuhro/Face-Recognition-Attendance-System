import face_recognition
import os
import pickle

dataset_path = "data/faces"
encodings = {}
for person in os.listdir(dataset_path):
    person_dir = os.path.join(dataset_path, person)
    person_encodings = []

    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        image = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(image)

        if face_locations:
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            person_encodings.append(encoding)

    if person_encodings:
        encodings[person] = person_encodings

# Save encodings
with open("data/encodings.pkl", "wb") as f:
    pickle.dump(encodings, f)

print("[INFO] Face encodings saved.")
