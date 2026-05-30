# RobotFace: Real-Time Biometric Tracking & Interactive UI

## 📌 Project Overview
RobotFace is an interactive computer vision application that bridges advanced facial recognition with a dynamic, asynchronous graphical interface. 

The system acts as a digital entity that actively tracks human movement in real-time, processes facial landmarks, and performs biometric authentication to greet recognized users via Text-to-Speech (TTS), all while maintaining a smooth 60 FPS UI rendering.

## 🎥 Video Demonstration
Watch the facial tracking, biometric authentication, and asynchronous eye movement in action:

https://github.com/user-attachments/assets/4468b614-1ef8-4166-8b9e-8d1de0057775

## 🛠️ Tech Stack & Tools
* **Computer Vision & Biometrics:** `OpenCV`, `MediaPipe` (Face Mesh), `face_recognition`.
* **Frontend (UI/UX):** `Flet` (Canvas API).
* **Concurrency & Execution:** `asyncio`, `threading`.
* **Audio Feedback:** `pyttsx3` (TTS).

## 🧠 System Architecture & Key Implementations

To prevent the heavy mathematical processing of computer vision from freezing the graphical interface, the application was designed with a highly decoupled, concurrent architecture:

### 1. Vision System (Backend - Threading)
* **Facial Landmark Tracking:** Utilizes `MediaPipe FaceMesh` to extract specific facial coordinates (e.g., the nose apex). These coordinates are mathematically normalized and mapped to target vectors for the digital eyes to follow.
* **Biometric Authentication:** Implements `face_recognition` to generate 128-dimension face encodings. The system compares real-time camera frames against a local database of known encodings to verify identity.
* **Daemon Threading:** The entire vision pipeline and the Text-to-Speech engine run on parallel background threads, ensuring the camera feed is processed without blocking the main application.

### 2. JarvisBrain UI (Frontend - Asyncio)
* **Asynchronous Rendering:** The Flet frontend runs on an `asyncio` event loop. It yields control (`await asyncio.sleep(0.016)`) to ensure the UI remains responsive and fluid.
* **Mathematical Interpolation:** Instead of snapping the digital eyes directly to the target coordinates, the system uses linear interpolation (`current_look += (target - current_look) * 0.1`) to create organic, smooth tracking movements.
* **Dynamic Canvas:** Procedural generation of the interface using Flet's Canvas shapes, including programmed blinking logic and emotional state transitions (e.g., smiling when a recognized user is authenticated).

## 🚀 How to Run
To run this project locally, ensure you have the required computer vision libraries installed:
```bash
pip install flet opencv-python mediapipe face_recognition pyttsx3
