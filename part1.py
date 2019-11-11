#step1: to analyse the saved image

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("hello.png")

cv2.imshow("Image", img)

cv2.waitKey(0)