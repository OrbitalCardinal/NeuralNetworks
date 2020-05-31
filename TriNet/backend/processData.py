import numpy as np 
import sys
import getData
import NeuralNetworks as NN
import ConvNet as CN
import Kernels
try:
    #Preparing input data
    input_dimension = int(sys.argv[2]) ** 2
    input_data = getData.parseRequestData(sys.argv[1], sys.argv[2])
    
    #Intantiate Conv Layers
    ConvLayers = CN.ConvNet(
        [
            [["Convolution",Kernels.diagonal_left,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
            [["Convolution",Kernels.cross,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
            [["Convolution",Kernels.diagonal_right,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
            [["Convolution",Kernels.horizontal_line,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]],
            [["Convolution",Kernels.vertical_line,False], ["RELU"], ["Pooling",2,2], ["Pooling",2,2]]
        ]
    )
    
    result = ConvLayers.process()
    #Intantiate Network from saved files
    # weights = getData.readData("./backend/weights.txt")
    # biases = getData.readData("./backend/biases.txt")
    # neurons, activation, error, learning_rate = getData.readArchitecture("./backend/architecture.txt")
    # NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate, weights=weights, biases=biases)
    # print(NN1.predict(input_data).item())
except Exception as e:
    print(e)

