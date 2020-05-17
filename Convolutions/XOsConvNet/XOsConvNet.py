import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv
import Kernels
import Convolutions
import Pooling
import RELU

def sigmoid(x):
    return(1/(1 + np.exp(-x)))
    
def multiPlotting(img_array, img_names):
    fig = plt.figure(figsize=(18,len(img_array)))
    ax = []
    for i in range(len(img_array)):
        ax.append(fig.add_subplot(1,len(img_array),i+1))
        ax[-1].set_title(img_names[i])
        for j in range(img_array[i].shape[0]):
            for k in range(img_array[i].shape[1]):
                ax[-1].text(k,j, "{:0.1f}".format(img_array[i][j,k]), ha="center", va="center",color="orange")
        plt.imshow(img_array[i],cmap="gray")
    fig.tight_layout()
    plt.show()
    

class ConvNet():
    def __init__(self,layers):
        self.layers = layers
    
    def process(self,inputImage):
        original_image = inputImage.copy()
        process_sequence = []
        img_names = []
        neurons_results = []
        for j in self.layers:
            inputImage = original_image.copy()
            for i in j:
                if i[0] == "Convolution":
                    inputImage = Convolutions.crossCorr2d(inputImage, i[1], padding=i[2])
                    # process_sequence.append(inputImage)
                    # img_names.append(i[0])
                elif i[0] == "Pooling":
                    inputImage = Pooling.max_pooling(inputImage,i[1],i[2])
                    # process_sequence.append(inputImage)
                    # img_names.append(i[0])
                elif i[0] == "RELU":
                    inputImage = RELU.RELU(inputImage)
                    # process_sequence.append(inputImage)
                    # img_names.append(i[0])
            # multiPlotting(process_sequence,img_names)
            neurons_results.append(inputImage)
        return np.array(neurons_results)
                 
XosNet = ConvNet(
    [
        [["Convolution",Kernels.diagonal_left,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
        [["Convolution",Kernels.cross,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
        [["Convolution",Kernels.diagonal_right,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]]
    ]
)
         
#Intialize weights and biases
weights = np.random.rand(12,2)  
bias = np.random.rand(1,2)

#Data
images = np.array(["X.png","X_S.png", "X_G.png", "X_A.png", "C.png", "C_S.png", "C_A.png", "C_G.png"])   
correct_result = np.array([[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1]])
            
# test_image = cv.imread("X.png",0)
# test_image = test_image/255
# test_image[test_image <= 0] = -1
# result_convs = XosNet.process(test_image).reshape(1,12)
# print(sigmoid(np.dot(result_convs,weights) + bias))