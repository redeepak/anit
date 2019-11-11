import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("DATA", obj.data)

    cv2.imshow("FRAME", frame)

    key = cv2.waitKey(1)        #if cv2.waitKey(1) & 0xFF('q'):
                                    #break
    if key == 27:
        break
        























