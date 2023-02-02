import cv2

def howSimilar(img1,img2):
    # test image
    histogram = cv2.calcHist([img1], [0],
                            None, [256], [0, 256])

    # data1 image
    histogram1 = cv2.calcHist([img2], [0],
                            None, [256], [0, 256])

    c1= 0

    # Euclidean Distance between data1 and test
    i = 0
    while i<len(histogram) and i<len(histogram1):
        c1+=(histogram[i]-histogram1[i])**2
        i+= 1
    c1 = c1**(1 / 2)

    return c1
