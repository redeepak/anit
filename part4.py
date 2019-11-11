#step4:import webcam

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break