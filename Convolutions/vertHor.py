import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import convs as conv
img = cv.imread("hor.png",0)
# img = cv.resize(img,(0,0),fx=0.3,fy=0.3)
img = np.array(img)

horizontal_kernel = np.array([
    [-1,-1,-1],
    [2,2,2],
    [-1,-1,-1]
])

vertical_kernel = np.array([
    [2,-1,-1],
    [2,-1,-1],
    [2,-1,-1]
])

img_vkernel = conv.crossCorr2d(img,vertical_kernel)
img_hkernel = conv.crossCorr2d(img,horizontal_kernel)

def sum_kernel(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j < 0:
                j = np.abs(j)
            count += j
    return count
