# author: JianHui Lin
# purpose: give las file and get the area and altitude of seleted building from the las data

import laspy
import numpy as np
import cv2

# read las file and get longitude, latitude, and altitude from it
inFile = laspy.file.File('17258975.las',mode='r')
longitude = inFile.x
latitude  = inFile.y
altitude = inFile.z

# get max and min of longitude, latitude and altitude
maxlong = np.amax(longitude)
minlong = np.amin(longitude)
maxlat = np.amax(latitude)
minlat = np.amin(latitude)
maxHeight = np.amax(altitude)
minHeight = np.amin(altitude)

# since each cell length is 8, so we divide 8 to get real number of rows and columns
col = int((maxlong-minlong)/8)
row = int((maxlat-minlat)/8)

matrix = np.zeros([row+2,col+2])
count = np.zeros([row+2,col+2])
img = np.zeros([row+2,col+2])
average = 0
pixels = 0
area = 0

# create a matrix
# set longitude as columns and set latitude as rows, and altitude is value of them
for i in range(len(altitude)):
    x = int(((longitude[i]-minlong)*((col-1)/(maxlong-minlong))))
    y = int(((latitude[i]-minlat)*((row-1)/(maxlat-minlat))))
    if count[y,x] == 0:
        matrix[y,x] += altitude[i]
        count[y,x] +=1

# get binary_img of building whose altitude is higher than middle level
for i in range(row):
    for j in range(col):
        if matrix[i,j] > (maxHeight + minHeight)/2 :
            img[i,j] = 1

# get number of pixel and average altitude for the selected building
endRow = int(row/1.9)
startCol = int(col/2)
newImg = np.zeros([int(row/1.9)+1,col])

for i in range(endRow):
    for j in range(startCol,col):
        if img[i,j] > 0:
            newImg[i,j-startCol] = 1
            average += matrix[i,j]
            pixels += 1

# get average of altitude
average /=pixels

# get area of the building
area = pixels * 64

print("the area of the selected building is: ", area)
print("the altitude of the selected building is: ", average)
