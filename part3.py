#step3: for only data


import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("hello.png")

decodedObjects = pyzbar.decode(img)

for obj in decodedObjects:
    print("DATA:", obj.data)

cv2.imshow("Image", img)

cv2.waitKey(0)