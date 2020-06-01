import numpy as np 
import sys
import getData
import NeuralNetworks as NN
import ConvNet as CN
import Kernels

# weights = getData.readData("./backend/weights.txt")
# biases = getData.readData("./backend/biases.txt")
weights = getData.readData("weights.txt")
biases = getData.readData("biases.txt")
# neurons, activation, error, learning_rate = getData.readArchitecture("./backend/architecture.txt")
neurons, activation, error, learning_rate = getData.readArchitecture("architecture.txt")
NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate, weights=weights, biases=biases)

#Preparing input data
inputs = getData.readData("trainingData.txt")
targets = getData.readData("targetData.txt")
n = 18
newInputs = []
for i in range(len(inputs)):
    counter = 0
    newMatrix = []
    for j in range(n):
        newRows = []
        for k in range(n):
            newRows.append(inputs[i][counter].item())
            counter += 1
        newMatrix.append(newRows)
    newMatrix = np.asarray(newMatrix)
    newInputs.append(newMatrix)

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

iterations = 200000
for i in range(iterations):
    actual_input = ConvLayers.process(newInputs[i % len(inputs)])
    actual_input = actual_input.flatten()
    actual_input = actual_input.reshape((len(actual_input),1))
    actual_target = targets[i % len(inputs)]
    NN1.train(actual_input, actual_target)
    print("MSE:", np.power(NN1.error,2).sum()/len(NN1.error))
    print(i)
print("Trained")
getData.storeData("weights.txt", NN1.weights,"w")
getData.storeData("biases.txt", NN1.biases,"w")