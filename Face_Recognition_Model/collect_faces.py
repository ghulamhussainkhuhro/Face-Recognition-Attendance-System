import cv2
import os

# Initialize video and face detector
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Get user name
name = input("Enter Your Name (use underscores instead of spaces, e.g., John_Doe): ").strip()

# Create folder to store this student's face images
data_path = os.path.join("data", "faces", name)
os.makedirs(data_path, exist_ok=True)

print("[INFO] Look into the camera. Turn your head slightly left, right, up, down.")
print("[INFO] Changing expressions slightly (neutral, smile, etc.) helps improve accuracy.")

count = 0
max_images = 100

while True:
    ret, frame = video.read()
    if not ret:
        print("[ERROR] Failed to capture frame. Exiting...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        resized_face = cv2.resize(face_img, (100, 100))  # Standard size for model

        # Save every detected face up to 100
        if count < max_images:
            file_path = os.path.join(data_path, f"{count}.jpg")
            cv2.imwrite(file_path, resized_face)
            count += 1

        # Draw rectangle and show progress
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"Images Captured: {count}/{max_images}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Collecting Faces", frame)
    key = cv2.waitKey(200)  # Wait 200ms between frames

    if key == ord('q') or count >= max_images:
        break

video.release()
cv2.destroyAllWindows()

print(f"[INFO] Collected {count} face images for '{name}'.")
