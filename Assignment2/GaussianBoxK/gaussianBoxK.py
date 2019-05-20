import cv2
import numpy as np



cv2.startWindowThread()
cv2.namedWindow("Original")
cv2.namedWindow("Normalized Box 9x9")
cv2.namedWindow("our own 9x9 kernel")
cv2.namedWindow("GaussianBlur")

# input image as grayscale
imgIn = cv2.imread("desktop.jpg", cv2.IMREAD_GRAYSCALE)

# The blur function does a normalized box filter.
nBoxFilter = cv2.blur(imgIn, (9,9) )
cv2.imwrite("Normalized.jpg", nBoxFilter)

kernel = np.ones( (9,9), np.float32)
kernel = kernel / 81

newImg= cv2.filter2D(imgIn, -1, kernel)
cv2.imwrite("kernel.jpg", newImg)

# Using the GaussianBlur funtion
gBlurImg = cv2.GaussianBlur(imgIn, (9,9), 1.7)
cv2.imwrite("GaussianBlur.jpg", gBlurImg)
