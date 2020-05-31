import numpy as np 
import sys
import getData
import NeuralNetworks as NN

# weights = getData.readData("./backend/weights.txt")
# biases = getData.readData("./backend/biases.txt")
weights = getData.readData("weights.txt")
biases = getData.readData("biases.txt")
# neurons, activation, error, learning_rate = getData.readArchitecture("./backend/architecture.txt")
neurons, activation, error, learning_rate = getData.readArchitecture("architecture.txt")
NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate, weights=weights, biases=biases)

iterations = 10000

inputs = getData.readData("trainingData.txt")
targets = getData.readData("targetData.txt")

for i in range(iterations):
    random = np.random.choice(range(len(inputs)))
    actual_input = inputs[random]
    actual_target = targets[random]
    NN1.train(actual_input, actual_target)
print("Trained")
getData.storeData("weights.txt", NN1.weights,"w")
getData.storeData("biases.txt", NN1.biases,"w")