```markdown
# 🎯 Face Recognition Attendance System

![Banner](https://repository-images.githubusercontent.com/588181932/e36ec678-7984-4cdd-8e4c-a3932772ff8e)

Welcome to the **Face Recognition Attendance System** — a smart solution for automating classroom or office attendance using facial recognition technology. Developed using **OpenCV**, this project combines the power of computer vision with efficient data handling to recognize faces, mark attendance, and handle unknown entries as "Anonymous."

---

## 🚀 Features

- 📸 Real-time face detection using OpenCV  
- 🧠 Face recognition using **PCA** (Principal Component Analysis) and **KNN** (K-Nearest Neighbors)  
- 📁 Dataset creation by capturing 50+ face images per individual  
- 🕵️ Labels unknown faces as **"Anonymous"**  
- ✅ Attendance is auto-marked for recognized individuals  
- 📦 Data stored and retrieved for consistent accuracy  
- 🖥️ Simple and beginner-friendly UI (console-based)  

---

## 🧰 Tech Stack

- **Language**: Python  
- **Libraries**: OpenCV, NumPy, OS, CSV  
- **Recognition Algorithm**: PCA + KNN  
- **Future Scope**:
  - Replace PCA+KNN with **LBPH** or **Deep Learning (FaceNet / Dlib)**
  - GUI Integration using Tkinter or Streamlit
  - Cloud-based attendance logs and dashboard  

---

## 📸 Screenshots

> _Coming soon: Sample screenshots/gifs of recognition in action!_

---

## 🧠 How It Works

1. **Data Collection**:
   - Capture multiple face images per student via webcam  
2. **Training Phase**:
   - Apply PCA for feature extraction  
   - Train KNN for face classification  
3. **Recognition Phase**:
   - Recognize known faces in real time  
   - Label unknown faces as "Anonymous"  
4. **Attendance Logging**:
   - Automatically logs name, date, and time in a CSV file  

---

## 🛠️ Installation & Usage

```bash
# Clone this repository
git clone https://github.com/ghulamhussainkhuhro/face-recognition-attendance-system.git

# Navigate to project directory
cd face-recognition-attendance-system

# Install dependencies
pip install opencv-python numpy

# Run the system
python recognize.py
```

---

## 🙋‍♂️ Author

**Ghulam Hussain Khuhro**  
🚀 Data Scientist | AI Explorer | Future Architect of Intelligent Systems  

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ghulamhussainkhuhro)  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/ghulamhussainkhuhro)  
[![Portfolio](https://img.shields.io/badge/-Portfolio-FF5722?style=flat&logo=web&logoColor=white)](https://ghulamhussainkhuhro.github.io/)  
[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/@ghulamhussainkhuhro2.o)  

📫 **ghulamhussainkhuhro2.o@gmail.com**

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🌟 Show Your Support

If you liked this project, give it a ⭐ on GitHub and share it with your peers!
```
