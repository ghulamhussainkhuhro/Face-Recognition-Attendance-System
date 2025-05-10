import face_recognition
import cv2
import pickle
import numpy as np
import os
from datetime import datetime
import csv

# Load known face encodings
with open("data/encodings.pkl", "rb") as f:
    known_encodings = pickle.load(f)

video = cv2.VideoCapture(0)
attendance = set()

print("[INFO] Starting recognition. Press 'o' to mark attendance. Press 'q' to quit.")

while True:
    ret, frame = video.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Anonymous"
        for person, enc_list in known_encodings.items():
            matches = face_recognition.compare_faces(enc_list, face_encoding, tolerance=0.5)
            if True in matches:
                name = person
                attendance.add(person)
                break

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)
    key = cv2.waitKey(1)

    if key == ord('o'):
        date = datetime.now().strftime("%d-%m-%Y")
        time = datetime.now().strftime("%H:%M:%S")
        os.makedirs("attendance", exist_ok=True)
        filepath = f"attendance/Attendance_{date}.csv"

        with open(filepath, 'a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["Name", "Time"])
            for person in attendance:
                writer.writerow([person, time])
        print("[INFO] Attendance marked.")
        attendance.clear()

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
