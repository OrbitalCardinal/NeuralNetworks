import numpy as numpy
import matplotlib.pyplot as plt
import cv2 as cv
import convs as convolution
import vertHor as vertHor

square = cv.imread("square.png",0)
square  = convolution.crossCorr2d(square,vertHor.horizontal_kernel)
plot = plt.imshow(square)
plot.set_cmap("gray")
plt.show()

