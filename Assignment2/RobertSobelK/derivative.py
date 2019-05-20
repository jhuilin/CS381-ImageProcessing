import cv2
import numpy as np

# robert
def robert_suanzi(img):
    r, c = img.shape
    r_sunnzi = [[-1,-1],[1,1]]
    for x in range(r):
        for y in range(c):
            if (y + 2 <= c) and (x + 2 <= r):
                imgChild = img[x:x+2, y:y+2]
                list_robert = r_sunnzi*imgChild
                img[x, y] = abs(list_robert.sum())
    return img

# # sobel
def sobel_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    new_imageX = np.zeros(img.shape)
    new_imageY = np.zeros(img.shape)
    s_suanziX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    s_suanziY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    for i in range(r-2):
        for j in range(c-2):
            new_imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziX))
            new_imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziY))
            new_image[i+1, j+1] = (new_imageX[i+1, j+1]*new_imageX[i+1,j+1] + new_imageY[i+1, j+1]*new_imageY[i+1,j+1])**0.5
    return np.uint8(new_image)

# Laplace
def Laplace_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    L_sunnzi = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    # L_sunnzi = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    for i in range(r-2):
        for j in range(c-2):
            new_image[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * L_sunnzi))
    return np.uint8(new_image)


img = cv2.imread('desktop.jpg', cv2.IMREAD_GRAYSCALE)

# robert
robert = robert_suanzi(img)
cv2.imwrite('robert.jpg',robert)

# sobel
sobel = sobel_suanzi(img)
cv2.imwrite('sobel.jpg',sobel)

# Laplace
laplace = Laplace_suanzi(img)
cv2.imwrite('laplace.jpg',laplace)
