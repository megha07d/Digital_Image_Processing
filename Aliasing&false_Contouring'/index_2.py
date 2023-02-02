
# Meghana Manvitha Venna
# CS20B1060

""" 
Down sample the grayscale Lena image with 8 different intensity ranges of values (0-
255, 0-128, 0-64, 0-32, 0-16, 0-8, 0-4, and 0-2). (Note: Size of images are the same).
And display all those 8 downsampled images in the same size display area on the
screen. Observe what happens.
"""

# (0-255, 0-128, 0-64, 0-32, 0-16, 0-8, 0-4, and 0-2).

import cv2 as cv
import numpy as np

img = cv.imread('Lenna.png')
print(f'Img shape is : {img.shape}')

cv.imshow('Lenna-original',img)

# gray img
img1 = cv.cvtColor(src = img,code = cv.COLOR_BGR2GRAY)

# intensity 0 - 1
img2 = img1
img2 = img2/255

# returns image with specified Intensity level
def intensifyTo(img,level):
    imgNew = (img * level).astype(np.uint8)
    return imgNew

# Different Intensity Levels
levels = [255,128,64,32,16,8,4,2]

for l in levels:
    img = intensifyTo(img2,l)
    img_name = f'Lenna-Gray-[0-{l}]'
    cv.imshow(img_name,img)

cv.waitKey(0)
cv.destroyAllWindows()


# OBSERVATION

# > As the range of intensity level is decreasing, Image turns darker and darker - smaller pixels
# > 2,4,8 intensity level images are barely visible, from 16,32,64,.. we can find the image grow brighter - larger pixels