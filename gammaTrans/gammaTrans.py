import cv2
from skimage import exposure
from matplotlib import pyplot as plt
import numpy as np

# read images
imgOver = cv2.imread('over.jpg',0)
imgUnder = cv2.imread('under.jpg',0)

# if its color images then transform them to gray then apply adjust_gamma to make transformation
# if input images is gray, then just apply adjust_gamma to make transformation
if len(imgOver.shape) >=3:
    grayOver = cv2.cvtColor(imgOver, cv2.COLOR_BGR2GRAY)
    gammaOver = exposure.adjust_gamma(grayOver, 4)
else:
    gammaOver = exposure.adjust_gamma(imgOver, 4)

if len(imgUnder.shape) >=3:
    grayUnder = cv2.cvtColor(imgUnder, cv2.COLOR_BGR2GRAY)
    gammaUnder = exposure.adjust_gamma(grayUnder, 0.5)
else:
    gammaUnder = exposure.adjust_gamma(imgUnder, 0.5)

# save gamma transform image to local file
cv2.imwrite('gamma_over.jpg',gammaOver)
cv2.imwrite('gamma_under.jpg',gammaUnder)

# calculate the histogram of four images
hist_over = cv2.calcHist([imgOver],[0],None,[256],[0,256])
hist_under = cv2.calcHist([imgUnder],[0],None,[256],[0,256])
histgamma_over = cv2.calcHist([gammaOver],[0],None,[256],[0,256])
histgamma_under = cv2.calcHist([gammaUnder],[0],None,[256],[0,256])

plt.plot(hist_over)         # blue in histogram
plt.plot(hist_under)        # orange in histogram
plt.plot(histgamma_over)    # green in histogram
plt.plot(histgamma_under)   # red in histogram
plt.show()
