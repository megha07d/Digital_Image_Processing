
# Meghana Venna
# CS20B1060

# BILINEAR INTERPOLATION FOR ZOOMING OR SHRINKING IMAGES
# WRITTEN CODE AND BUILT-IN FUNCTIONS

import cv2 as cv

# 1. Load image
img = cv.imread('Lenna.png')

# 2. convert to gray image
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 3. get matrix
# print(img.shape)

# 4. Get scale
scale = float(input('Enter scale: '))

# 5. make new scaled matrix
import numpy as np
import math

new_size = int(scale*img.shape[1])
img2 = np.zeros((new_size,new_size)) 

# cv.imshow('Final image',img2)

# CODED
# 6. Assign vals to new image pixels
x_bound = img.shape[1]


import pixel

for i in range(0,new_size):
    for j in range(0,new_size):
        img2[i][j]= pixel.getPixel(i,j,x_bound,img,scale)

uint_img = img2.astype('uint8')

# BUILT-IN
img3 = cv.resize(img,None, fx = scale, fy = scale, interpolation = cv.INTER_LINEAR)

# DISPLAY IMAGES
cv.imshow('Lenna',img)
cv.imshow('Coded Bi-linear Lenna',uint_img)
cv.imshow('Built-in Bi-linear Lenna',img3)


cv.waitKey(0)
cv.destroyAllWindows()
