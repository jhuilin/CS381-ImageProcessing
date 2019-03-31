#author: JianHui Lin
#purpose: input one only background image, and one same background
#         image with object, compare two picture to get the object
#         intensity value and display its hitogram and binary image
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
# get input images from user
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second input image")
args = vars(ap.parse_args())
img1 = cv2.imread(args["first"])
img2 = cv2.imread(args["second"])

row, col, band = img1.shape
gray_img1 = np.zeros([row,col])
gray_img2 = np.zeros([row,col])
object = np.zeros([row,col])
binary_img = np.zeros(256)
x = np.arange(0,256)

# convert to grayscale picture
for i in range (row):
  for j in range(col):
      gray_img1[i,j] = int(img1[i,j,0]*0.07 + img1[i,j,1]*0.72 + img1[i,j,2]*0.21)
      gray_img2[i,j] = int(img2[i,j,0]*0.07 + img2[i,j,1]*0.72 + img2[i,j,2]*0.21)
      # get gray image only contain object
      object[i,j] = abs(gray_img1[i,j] - gray_img2[i,j])
      # convert to binary image
      if(abs(gray_img1[i,j] - gray_img2[i,j])> 110):
        object[i,j]=255
      else:
        object[i,j]=0
      # get histogram of binary image
      binary_img[int(object[i,j])] +=1

cv2.imwrite('binary_image.png', object)

plt.bar(x,binary_img,color="black")
plt.title("Hisogram of picture")
plt.show()
