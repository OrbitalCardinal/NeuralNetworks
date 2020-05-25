import numpy as np 
import NeuralNetworks as NN
import matplotlib.pyplot as plt

def function(x):
    return 1 + np.sin(6*np.pi/4* x)

#Architecture
neurons = [1,60,60,60,1]
activation = ["sigmoid","linear","sigmoid","linear"]
error = "SE"
#weights and biases initialization
w1 = np.matrix([[-0.27],[-0.41]])
w2 = np.matrix([[0.09, -0.17]])
b1 = np.matrix([[-0.48],[-0.13]])
b2 = np.matrix([[0.48]])
#Network params
weights = [w1,w2]
biases = [b1,b2]
lr = 0.01 #Learning rate
#training set
x1 = np.arange(-2,2,0.01)
# NN1 = NN.NeuralNetwork(neurons, activation,error,lr,weights=weights, biases=biases)
NN1 = NN.NeuralNetwork(neurons,activation,error,lr)
iterations = 200
counter = 0
for i in range(iterations):
    inputs = np.matrix([[np.random.choice(x1)]])
    # inputs = np.matrix([[x1[counter % len(x1)]]])
    # inputs = np.matrix([[1]])
    t = function(inputs)
    NN1.train(inputs,t)
    counter += 1
    print("SE:", np.power(NN1.error,2).sum()/len(NN1.error))
    

y1 = function(x1)
y2 = []
for i in x1:
    y2.append(NN1.predict(np.matrix([[i]])).item())
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.show()

    

