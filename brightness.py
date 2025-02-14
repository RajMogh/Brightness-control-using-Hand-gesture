import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc

def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            h, w, _ = frame.shape
            
            thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))
            index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
            
            distance = calculate_distance(thumb_tip, index_tip)
            brightness = np.clip(distance / 2, 0, 100)
            sbc.set_brightness(int(brightness))
            
            cv2.putText(frame, f'Brightness: {int(brightness)}%', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
