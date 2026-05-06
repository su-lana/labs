import cv2
import numpy as np

img = cv2.imread('img.jpg')

kernel1 = np.array([
    [ 0, -1,  0],
    [-1,  6, -1],
    [ 0, -1,  0]
])

sharpened = cv2.filter2D(img, -1, kernel1)

blurred = cv2.GaussianBlur(img, (11, 11), 0)
 
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()