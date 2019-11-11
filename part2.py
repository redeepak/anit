#step2: creating qr detector using pyzbar


import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("hello.png")

decodedObjects = pyzbar.decode(img)

print(decodedObjects)

cv2.imshow("Image", img)

cv2.waitKey(0)