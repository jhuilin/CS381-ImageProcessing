#author: JianHui Lin
#purpose: input a image and display its histogram with color red, green, blue and gray

import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def calcHist(img):
    row, col, band = img.shape
    gray_img = np.zeros([row,col])
    red = np.zeros(256)
    green = np.zeros(256)
    blue = np.zeros(256)
    gray = np.zeros(256)
    x = np.arange(0,256)

    #convert to grayscale picture
    for i in range (row):
        for j in range(col):
            gray_img[i,j] = img[i,j,0]*0.07 + img[i,j,1]*0.72 + img[i,j,2]*0.21

    # get histogram of red, green, blue and gray
    for i in range (row):
       for j in range(col):
           red[img[i,j,2]] += 1
           green[img[i,j,1]] += 1
           blue[img[i,j,0]] += 1
           gray[int(gray_img[i,j])] +=1

    # display red, green, blue and gray histogram
    plt.bar(x,red,color="red")
    plt.bar(x,green,color="green")
    plt.bar(x,blue,color="blue")
    plt.bar(x,gray,color="gray")
    plt.title("Hisogram of picture")
    plt.show()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--first", required=True, help="first input image")
    args = vars(ap.parse_args())
    img = cv2.imread(args["first"])       #user input the image
    calcHist(img)

main()
