#Fully connected layers
import numpy as np

class NeuralNetwork():
    def __init__(self,layers,neurons,activation,error_function,weights,biases,learning_rate):
        self.layers = layers #number of layers
        self.neurons = neurons #number of neurons per layer
        self.activation = activation
        self.error_function = error_function #Error function
        self.weights = weights
        self.biases = biases
        self.learning_rate = learning_rate
        self.success_rate = None
    
    def train(self,inputs, target):
        self.outputs = [inputs]
        self.deltas = []
        self.forwardPass()
        self.backwardPass(target)
        self.weightsUpdate()
        
        
    def forwardPass(self):
        for i in range(self.layers):
            if self.activation[i] == "sigmoid":
                self.outputs.append(self.sigmoid(self.weights[i]*self.outputs[-1] + self.biases[i]))
            elif self.activation[i] == "linear":
                self.outputs.append(self.linear(self.weights[i]*self.outputs[-1] + self.biases[i]))
            
    
    def backwardPass(self,targets):
        self.error = targets - self.outputs[-1]
        for i in range(self.layers):
            jacobian = self.jacobian(self.neurons[-1-i], self.activation[-1-i],self.outputs[-1-i])
            if i == 0:
                if self.error_function == "SE":
                    s = -2 * jacobian * (targets - self.outputs[-1-i])
                elif self.error_function == "MSE":
                    s = jacobian * (self.outputs[-1-i] - targets)
            else:
                s = jacobian * self.weights[i].T * self.deltas[-1]
            self.deltas.append(s)
    
    def weightsUpdate(self):
        for i in range(self.layers):
            self.weights[self.layers-1-i] -= self.learning_rate * self.deltas[i] * self.outputs[-2-i].T
    
    def predict(self,input):
        for i in range(self.layers):
            if self.activation[i] == "sigmoid":
                input = self.sigmoid(self.weights[i]*input + self.biases[i])
            elif self.activation[i] == "linear":
                input = self.linear(self.weights[i]*input + self.biases[i])
        return input
        
    
    def sigmoid(self,x,deriv = False):
        if deriv:
            return x * (1 - x)
        return 1/(1 + np.exp(-x))
    
    def linear(self,x, deriv = False):
        if deriv:
            return 1
        return x
    
    def jacobian(self,neurons,activation,x):
        result = np.zeros((neurons,neurons))
        x_counter = 0
        for i in range(neurons):
            for j in range(neurons):
                if i == j:
                    if activation == "sigmoid":
                        result[i,j] = self.sigmoid(x[x_counter],deriv=True)
                    elif activation == "linear":
                        result[i,j] = self.linear(x[x_counter],deriv=True)
                    x_counter += 1
        return result
        
#Data
# inputs = np.matrix([[0.05],[0.10]])
# t = np.matrix([[0.01],[0.99]])
# w1 = np.matrix([[0.15,0.20],[0.25,0.30]])
# w2= np.matrix([[0.40,0.45],[0.50,0.55]])
# b1 = 0.35
# b2 = 0.60
# inputs = np.matrix([[1]])
# t = 1 + np.sin((np.pi/4)*inputs)
# w1 = np.matrix([[-0.27],[-0.41]])
# w2 = np.matrix([0.09, -0.17])
# b1 = np.matrix([[-0.48],[-0.13]])
# b2 = np.matrix([[0.48]])
# #Architecture
# layers = 2
# neurons = [2,1]
# activation = ["sigmoid","linear"]
# error = "SE"
# #Network params
# weights = [w1,w2]
# outputs = [inputs]
# biases = [b1,b2]
# lr = 0.1 #Learning rate
# iterations = 100
# CNN1 = NeuralNetwork(layers,neurons, activation,error,weights,biases, lr)
# for i in range(iterations):
#     CNN1.train(inputs,t)
#     print("MSE:", np.power(CNN1.error,2).sum()/len(CNN1.error))
# print(CNN1.predict(np.matrix([[1]])))
# print(t)



        
