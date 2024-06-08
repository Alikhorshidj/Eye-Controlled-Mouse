import cv2
import mediapipe as mp
import time



cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks:
            x = landmark.x
            y = landmark.y
            print(x, y)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)