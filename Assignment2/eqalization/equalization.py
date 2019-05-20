import cv2
from matplotlib import pyplot as plt
import numpy as np

# read images
over = cv2.imread('over.jpg',0)
under = cv2.imread('under.jpg',0)

# if its color images then transform them to gray then equlizing them
# if input images is gray, then just equlizing them
if len(over.shape) >=3:
    grayOver = cv2.cvtColor(over, cv2.COLOR_BGR2GRAY)
    equ_over = cv2.equalizeHist(grayOver)
else:
    equ_over = cv2.equalizeHist(over)

if len(under.shape) >=3:
    grayUnder = cv2.cvtColor(under, cv2.COLOR_BGR2GRAY)
    equ_under = cv2.equalizeHist(grayUnder)
else:
    equ_under = cv2.equalizeHist(under)

# save equalized images in local file
cv2.imwrite('equ_over.jpg',equ_over)
cv2.imwrite('equ_under.jpg',equ_under)

# calculate the histogram of four images
hist_over = cv2.calcHist([over],[0],None,[256],[0,256])
hist_under = cv2.calcHist([under],[0],None,[256],[0,256])
hist_equ_over = cv2.calcHist([equ_over],[0],None,[256],[0,256])
hist_equ_under = cv2.calcHist([equ_under],[0],None,[256],[0,256])

plt.plot(hist_over)         # blue line in histogram
plt.plot(hist_under)        # orange line in histogram
plt.plot(hist_equ_over)     # green line in histogram
plt.plot(hist_equ_under)    # red line in histogram
plt.show()
