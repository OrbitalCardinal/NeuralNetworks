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
    padding = False
    ConvLayers = CN.ConvNet(
    [
        [["Convolution", Kernels.diagonal_left, padding] ],
        [["Convolution", Kernels.diagonal_right, padding]],
        [["Convolution", Kernels.vertical_line, padding]],
        [["Convolution", Kernels.horizontal_line, padding]]
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
    # print(np.argmax(NN1.predict(result)))
    print(st.ascii_lowercase[np.argmax(NN1.predict(result))])
except Exception as e:
    print("Final error:",e)

