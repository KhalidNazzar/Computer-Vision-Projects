import cv2
import mediapipe as mp
import numpy as np
import os
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 5)
width, height = 1280, 720
cap.set(3, width)
cap.set(4, height)

imgCanvas = np.zeros((height, width, 3), np.uint8)

folderPath = '/home/khalid/Videos/Hand_Tracking_Project/Header'
overlayList = [cv2.imread(f'{folderPath}/{imPath}') for imPath in os.listdir(folderPath)]

header = overlayList[0]
drawColor = (0, 0, 255)
thickness = 20
tipIds = [4, 8, 12, 16, 20]
xp, yp = 0, 0

with mp_hands.Hands(min_detection_confidence=0.85, min_tracking_confidence=0.5, max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                points = [[int(lm.x * width), int(lm.y * height)] for lm in hand_landmarks.landmark]

                fingers = []
                if points[tipIds[0]][0] < points[tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for id in range(1, 5):
                    if points[tipIds[id]][1] < points[tipIds[id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                if fingers[1] and fingers[2] and all(fingers[i] == 0 for i in [0, 3, 4]):
                    xp, yp = points[8]
                    if points[8][1] < 125:
                        if 170 < points[8][0] < 295:
                            header = overlayList[0]
                            drawColor = (0, 0, 255)
                        elif 436 < points[8][0] < 561:
                            header = overlayList[1]
                            drawColor = (255, 0, 0)
                        elif 700 < points[8][0] < 825:
                            header = overlayList[2]
                            drawColor = (0, 255, 0)
                        elif 980 < points[8][0] < 1105:
                            header = overlayList[3]
                            drawColor = (0, 0, 0)

                if fingers[1] and fingers[4] and all(fingers[i] == 0 for i in [0, 2, 3]):
                    cv2.line(image, (xp, yp), (points[20][0], points[20][1]), drawColor, 5) 
                    xp, yp = points[8]

                if fingers[1] and all(fingers[i] == 0 for i in [0, 2, 3, 4]):
                    cv2.circle(image, (points[8][0], points[8][1]), int(thickness/2), drawColor, cv2.FILLED)
                    if xp == 0 and yp == 0:
                        xp, yp = points[8]
                    cv2.line(imgCanvas, (xp, yp), (points[8][0], points[8][1]), drawColor, thickness)
                    xp, yp = points[8]

                if fingers[0] and fingers[4] and all(fingers[i] == 0 for i in [1, 2, 3]):
                    imgCanvas = np.zeros((height, width, 3), np.uint8)
                    xp, yp = points[8]

        image[0:125, 0:width] = header
        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 5, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(image, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

        cv2.imshow('MediaPipe Hands', img)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
