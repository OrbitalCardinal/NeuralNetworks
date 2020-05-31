import numpy as np 
import Kernels
import Convolutions
import Pooling
import RELU

class ConvNet():
    def __init__(self,layers):
        self.layers = layers
    
    def process(self,inputImage):
        original_image = inputImage.copy()
        neurons_results = []
        for j in self.layers:
            inputImage = original_image.copy()
            for i in j:
                if i[0] == "Convolution":
                    inputImage = Convolutions.crossCorr2d(inputImage, i[1], padding=i[2])
                elif i[0] == "Pooling":
                    inputImage = Pooling.max_pooling(inputImage,i[1],i[2])
                elif i[0] == "RELU":
                    inputImage = RELU.RELU(inputImage)
            neurons_results.append(inputImage)
        return np.array(neurons_results)
                 
# XosNet = ConvNet(
#     [
#         # [["Convolution",Kernels.diagonal_left,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]]
#         [["Convolution",Kernels.diagonal_left,False]]
#     ]
# )
# test = np.array([
#         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
#         [-1, 1,-1,-1,-1,-1,-1, 1,-1],
#         [-1,-1, 1,-1,-1,-1, 1,-1,-1],
#         [-1,-1,-1, 1,-1, 1,-1,-1,-1],
#         [-1,-1,-1,-1, 1,-1,-1,-1,-1],
#         [-1,-1,-1, 1,-1, 1,-1,-1,-1],
#         [-1,-1, 1,-1,-1,-1, 1,-1,-1],
#         [-1, 1,-1,-1,-1,-1,-1, 1,-1],
#         [-1,-1,-1,-1,-1,-1,-1,-1,-1]
#     ])
# result_convs = XosNet.process(test)
# print(result_convs[0])