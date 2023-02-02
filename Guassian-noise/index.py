# Meghana Manvitha
# cs20b1060

# Observation : 
# Resemblance to original image incraeses as more num of noisy images are added - 'g' becomes more 'f' as 'i' increases
# To get most similar image to original one, its a better choice to add as many noisy images as possible


import cv2 as cv
import numpy as np
import random

# uint8 holds only 0-255 vals 

# fxn to find out how similar imgs are
def howSimilar(img1,img2):
    # test image
    histogram = cv.calcHist([img1], [0],
                            None, [256], [0, 256])

    # data1 image
    histogram1 = cv.calcHist([img2], [0],
                            None, [256], [0, 256])

    c1= 0

    # Euclidean Distance between data1 and test
    i = 0
    while i<len(histogram) and i<len(histogram1):
        c1+=(histogram[i]-histogram1[i])**2
        i+= 1
    c1 = c1**(1 / 2)

    return c1


# 1. read image
img1 = cv.imread('Lenna.png')

# 2. convert to gray image
img2 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

# 3. make a gaussian image
a = img2.shape[0]
b = img2.shape[1]

# 4. input n

cv.imshow('Lenna Original',img2)

distances = []

n_vals1 = range(5,100,5)
n_vals = [5,10,20,30,50]
for n in n_vals1:
    # 5. generate f(i)'s  
    # genearting f(i)'s

# sums is not uint8 - to accomadate sum of all pimage pixels. later normalised
    sums = np.zeros((a,b),dtype=np.int)

    for i in range(n):
        # 3.1 numpy array with zeroes
        gauss_noise = np.zeros((a,b),dtype=np.uint8)

        # 3.2 fill with guass distrib vals
        cv.randn(gauss_noise,mean = random.randint(0,255), stddev=random.randint(0,50))

        gauss_noise = (0.5*gauss_noise).astype(np.uint8)

        # gauss is f[i]
        gauss_img = cv.add(img2,gauss_noise)

        # uncomment below line if you want to see each gaussian image generated
        # cv.imshow(f'Lenna Gaussian - {i}',gauss_img)
        # sum
        sums = sums + gauss_img

    # finding avg image - g
    sums = sums/n

    # range : [0,255]

    # print(np.amin(sums),np.amax(sums))

    sums = sums.astype(np.uint8)

    # print(np.amin(sums),np.amax(sums))

    cv.imshow(f'Lenna Gaussian avg for n={n}',sums)

    # calculate how similar are 'sums' and img2 - metric : eucledian
    d = howSimilar(img2,sums)

    # list of dist's
    distances.append(d)
    print(f'Distance for n = {n} is {d}')


cv.waitKey(0)
cv.destroyAllWindows()

# plot n-valye vs similarity
import matplotlib.pyplot as plt
plt.plot(n_vals1,distances,marker='o')
plt.xlabel('n - num of noisy images')
plt.ylabel('Resemblance of g with f')
plt.title('similarity vs n')
plt.show()

# we can see that resemblance to original image incraeses as more num of noisy images are added - in general