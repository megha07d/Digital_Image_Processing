print(5/2.5 * 3)
print(5//2)

import cv2 as cv

# 1. Load image
img = cv.imread('Lenna.png')

# 2. convert to gray image
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

print(img[3][10])

# damn cool u can zoom in and see pixel values !!!