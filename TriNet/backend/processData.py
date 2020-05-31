import numpy as np 
import sys
import getData
import NeuralNetworks as NN
import ConvNet as CN
import Kernels
import string as st
try:
    #Preparing input data
    input_data = getData.parseRequestData(sys.argv[1], sys.argv[2], "c")
    
    # Intantiate Conv Layers
    ConvLayers = CN.ConvNet(
        [
            [["Convolution", Kernels.diagonal_left, False], ["RELU"], ["Convolution", Kernels.diagonal_left, False], ["RELU"], ["Pooling",2,2],["Convolution", Kernels.diagonal_left, False],["RELU"], ["Pooling",2,2]],
            [["Convolution", Kernels.cross, False], ["RELU"], ["Convolution", Kernels.cross, False], ["RELU"], ["Pooling",2,2],["Convolution", Kernels.cross, False],["RELU"], ["Pooling",2,2]],
            [["Convolution", Kernels.diagonal_right, False], ["RELU"], ["Convolution", Kernels.diagonal_right, False], ["RELU"], ["Pooling",2,2],["Convolution", Kernels.diagonal_right, False],["RELU"], ["Pooling",2,2]],
            [["Convolution", Kernels.vertical_line, False], ["RELU"], ["Convolution", Kernels.vertical_line, False], ["RELU"], ["Pooling",2,2],["Convolution", Kernels.vertical_line, False],["RELU"], ["Pooling",2,2]],
            [["Convolution", Kernels.horizontal_line, False], ["RELU"], ["Convolution", Kernels.horizontal_line, False], ["RELU"], ["Pooling",2,2],["Convolution", Kernels.horizontal_line, False],["RELU"], ["Pooling",2,2]]
        ]
    )    
    result = ConvLayers.process(input_data)
    result = result.flatten()
    result = result.reshape((len(result),1))
    
    #Intantiate Network from saved files
    weights = getData.readData("./backend/weights.txt")
    biases = getData.readData("./backend/biases.txt")
    neurons, activation, error, learning_rate = getData.readArchitecture("./backend/architecture.txt")
    NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate, weights=weights, biases=biases)
    # print(st.ascii_lowercase[np.argmax()])
    print(NN1.predict(result))
except Exception as e:
    print("Final error:",e)

