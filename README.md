# Hand Gesture-Based Brightness Control

## Overview
This project enables users to control their screen brightness using hand gestures. It utilizes OpenCV and MediaPipe for real-time hand tracking and adjusts brightness dynamically based on the distance between the thumb and index finger.

## Features
- **Real-time Hand Tracking:** Uses OpenCV and MediaPipe to detect hand landmarks.
- **Gesture-Based Control:** Adjusts screen brightness based on finger distance.
- **Dynamic Brightness Scaling:** Converts distance to brightness percentage.
- **Intuitive UI:** Displays brightness level on the screen.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gesture-brightness-control.git
   ```
2. Install required dependencies:
   ```bash
   pip install opencv-python mediapipe numpy screen-brightness-control
   ```
3. Run the application:
   ```bash
   python brightness_control.py
   ```

## Usage
- Hold your hand in front of the webcam.
- Adjust the distance between your **thumb** and **index finger** to increase or decrease brightness.
- The brightness level is displayed on the screen.
- Press `q` to exit the application.

## Technologies Used
- OpenCV (Computer Vision)
- MediaPipe (Hand Tracking)
- NumPy (Mathematical Operations)
- screen-brightness-control (Brightness Adjustment)



## Contact
For inquiries or suggestions, please reach out to amoghrajsinha@gmai.com.

