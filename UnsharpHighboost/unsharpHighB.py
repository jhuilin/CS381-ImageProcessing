import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("desktop.jpg", cv2.COLOR_BGR2GRAY)

gauss_mask = cv2.GaussianBlur(image, (9, 9), 10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)

cv2.imwrite("Sharpen.jpg", image_sharp)


kernel = np.array([[-1, -1, -1],

                   [-1,  8, -1],

                   [-1, -1, -1]])

image_hpf = cv2.filter2D(image, -1, kernel)

cv2.imwrite("HighPassFilter.jpg", image_hpf)
