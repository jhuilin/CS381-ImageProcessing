# author: JianHui Lin
# purpose: to generate an image in false color using the hyperspectral image

from spectral import *
import numpy as np
import cv2

# ignore divide by zero for ndvi
np.seterr(divide='ignore', invalid='ignore')

img = open_image('TIPJUL1.LAN')
row,col,bands = img.shape

# display false color photo
v1 = imshow(img,(3,2,1))

binary_img = np.zeros([row,col])
red =img[:,:,2]
nir = img[:,:,3]

# normalized the nir and red and calculate the ndvi
nir = (nir+128)/256
red = (red+128)/256
ndvi = (nir-red)/(nir+red)

# normalized the ndvi for ndvi > 0
for i in range(row):
    for j in range(col):
        if ndvi[i,j]>0:
            binary_img[i,j]=1

# output binary image
cv2.imshow('image',binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
