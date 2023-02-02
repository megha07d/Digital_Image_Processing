import cv2 as cv
import numpy as np

# 1. read image
img1 = cv.imread('Lenna.png')

# 2. convert to gray image
img2 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

cv.imshow('Lenna original',img2)

minPixel = np.amin(img2)
maxPixel = np.amax(img2)

print(minPixel,maxPixel)

# img2 = (img2/10).astype(np.uint8)

img = np.zeros((512,512),dtype=np.uint8)

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i][j] = img2[i][j] + 1000


for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i][j] = img2[i][j]/255

cv.imshow('Lenna operated',img)

minPixel = np.amin(img)
maxPixel = np.amax(img)
print(minPixel,maxPixel)

cv.waitKey(0)
