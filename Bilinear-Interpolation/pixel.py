import math

# Wortks for zooming and shrinking

def getPixel(i,j,thr,img,scale):

    m = i/scale
    n = j/scale

    # get pixel at m,n in img
    x1 = math.floor(m)
    x3 = x1

    x2 = math.ceil(m)
    x4 = x2

    y1 = math.ceil(n)
    y2 = y1

    y3 = math.floor(n)
    y4 = y3

    # if threshold is crossed
    if x1>thr-1 or x2>thr-1 or y1>thr-1 or y3>thr-1 :
        return 0
    elif x1==x2 and y1!=y3:
        # m is int but not n
        # linearinterpolation on y-axis
        ans = (y2-n)* img[x3][y3] + (n-y3)*img[x2][y2]
        return ans
    elif x1!=x2 and y1==y3:
        # n is int but not m
        # linearinterpolation on x-axis
        ans = (m-x1)* img[x2][y2] + (x2-m)*img[x1][y1]
        return ans
    elif x1 == x2 and y1 == y3:
        # if both are ints
        return img[x1][y1]
        

    d1 = (m-x1) * (y1-n)
    d2 = (x2-m) * (y1-n)
    d3 = (n-y3) * (m-x1)
    d4 = (x2-m) * (n-y3)

    ans = img[x1][y1] * d4 + img[x2][y2] * d3 + img[x3][y3] * d2 + img[x4][y4] * d1

    # ans can be decimals
    # so cap it with ceil
    new_ans = math.ceil(ans)

    return new_ans
