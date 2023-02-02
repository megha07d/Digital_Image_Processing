
# Meghana Manvitha Venna
# CS201B060

""" 
Convert the given Lena image to grayscale image. Use the cv2.resize() to down sample
the image with 4 sizes (128*128, 64*64, 32*32, and 16*16). Display the original image,
and down sampled images with the same display size. Observe what happens.
"""

import cv2 as cv

# read and show image
img = cv.imread('Lenna.png')
cv.imshow('Lena 512',img)
print(img.shape)

# convert to gray scale
img1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Lena Gray',img1)

def resizeTo(img, level):
    imgNew = cv.resize(img1,(level,level),interpolation=cv.INTER_AREA)
    return imgNew

levels = [128,64,32,16]

for l in levels:
    img = resizeTo(img1,l)
    cv.imshow(f'Lena-size-{l}',img)
    print(f'Image[{l}] shape is : {img.shape}')

cv.waitKey(0)
cv.destroyAllWindows()


# OBSERVATION

# after 64, img size is same but pixel values are distorted
# when you reduce the size of an image, you are also reducing the number of pixels. 
# The more you reduce the number of pixels, the more you reduce the quality of the image