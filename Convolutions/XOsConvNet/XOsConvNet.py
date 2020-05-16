import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv
import Kernels
import Convolutions
import Pooling

class ConvNet():
    def __init__(self,layers):
        self.layers = layers
    
    def train(self,inputImage):
        #Normalize between -1 and 1
        inputImage = inputImage/255
        inputImage[inputImage <= 0] = -1
        
        for i in self.layers:
            if i == "Convolution":
                #Apply kernel
                inputImage = Convolutions.crossCorr2d(inputImage, Kernels.diagonal_left, padding=True)
            elif i == "Pooling":
                inputImage = Pooling.max_pooling(inputImage,1,1)
            
        return inputImage
    
            

original_image = cv.imread('X.png',0)
#Normalize between -1 and 1
original_image = (original_image/255)
original_image[original_image <= 0] = -1

#Apply kernel
filtered_image = Convolutions.crossCorr2d(original_image, Kernels.diagonal_left, padding=True)
#Pool
pooled_image = Pooling.max_pooling(filtered_image,2,2)

filtered_image = Convolutions.crossCorr2d(filtered_image, Kernels.diagonal_left, padding=True)
pooled_image = Pooling.max_pooling(filtered_image,1,1)

XosNet = ConvNet(["Convolution", "Pooling", "Convolution", "Pooling"])
print(XosNet.layers)

fig = plt.figure(figsize=(1,3))
ax = []
ax.append(fig.add_subplot(1,4,1))
ax[-1].set_title("Original image")
plt.imshow(original_image, cmap="gray")

ax.append(fig.add_subplot(1,4,2))
ax[-1].set_title("Filtered image")
plt.imshow(filtered_image, cmap="gray")

ax.append(fig.add_subplot(1,4,3))
ax[-1].set_title("Pooled image")
plt.imshow(pooled_image, cmap="gray")

ax.append(fig.add_subplot(1,4,4))
ax[-1].set_title("Network output")
plt.imshow(XosNet.train(original_image), cmap="gray")

plt.show()

