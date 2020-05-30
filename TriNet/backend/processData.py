import numpy as np 
import sys
import getData
import NeuralNetworks as NN
try:
    #Preparing input data
    input_dimension = int(sys.argv[2]) ** 2
    input_data = getData.parseRequestData(sys.argv[1], sys.argv[2])
    #Network arquitecture
    # neurons = [input_dimension, 2, 1]
    # activation = ["sigmoid", "sigmoid"]
    # error = "SE"
    # learning_rate = 0.01
    # getData.storeData(path, NN1.weights)
    weights = getData.readData("./backend/weights.txt")
    biases = getData.readData("./backend/biases.txt")
    neurons, activation, error, learning_rate = getData.readArchitecture("./backend/architecture.txt")
    NN1 = NN.NeuralNetwork(neurons, activation, error, learning_rate, weights=weights, biases=biases)
    print(NN1.predict(input_data).item())
    # for i in range(len(result)):
    #     print("file:",result[i].shape," object:",NN1.weights[i].shape)
except Exception as e:
    print(e)

