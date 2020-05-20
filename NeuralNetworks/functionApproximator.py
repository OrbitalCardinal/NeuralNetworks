import numpy as np 
import NeuralNetworks as NN
import matplotlib.pyplot as plt

def function(x):
    return 1 + np.sin(np.pi/4*x)

#Architecture
layers = 2
neurons = [2,1]
activation = ["sigmoid","linear"]
error = "MSE"
#weights and biases initialization
w1 = np.matrix([[-0.27],[-0.41]])
w2 = np.matrix([0.09, -0.17])
b1 = np.matrix([[-0.48],[-0.13]])
b2 = np.matrix([[-0.2]])
#Network params
weights = [w1,w2]
biases = [b1,b2]
lr = 0.01 #Learning rate
iterations = 100000
#training set
x1 = np.arange(-2,2,0.01)

NN1 = NN.NeuralNetwork(layers,neurons, activation,error,weights,biases, lr)
for i in range(iterations):
    inputs = np.matrix([[np.random.choice(x1)]])
    t = function(inputs)
    NN1.train(inputs,t)
    # print("MSE:", np.power(NN1.error,2).sum()/len(NN1.error))
    

y1 = function(x1)
y2 = []
for i in x1:
    y2.append(NN1.predict(i)[0,0])
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.show()
    

