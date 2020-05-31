import numpy as np
import getData
import NeuralNetworks as NN
import sys

n = 45

#Architecture
neurons = [n,n,n,26]
activation = ["sigmoid","sigmoid","sigmoid"]
error = "SE"
learning_rate = 0.01
NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate)
getData.storeData("weights.txt", NN1.weights,"w")
getData.storeData("biases.txt", NN1.biases,"w")

file = open("architecture.txt","w")
for i in range(len(neurons)):
    string = str(neurons[i])+","
    if i == len(neurons) - 1:
        string = str(neurons[i])
    file.write(string)
file.write("\n")
for i in range(len(activation)):
    string = activation[i]+","
    if i == len(activation) - 1:
        string = activation[i]
    file.write(string)
file.write("\n")
file.write(error+"\n")
file.write(str(learning_rate)+"\n")
file.close()
    