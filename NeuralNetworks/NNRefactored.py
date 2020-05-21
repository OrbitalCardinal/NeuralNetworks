import numpy as np 

class NeuralNetwork():
    def __init__(self, neurons,learning_rate,weights = None, biases = None):
        self.neurons = neurons
        self.layers = len(neurons)
        self.weights = weights
        self.biases = biases
        self.outputs = []
        self.deltas = []
        self.jacobians_list = []
        self.learning_rate = learning_rate
        if not self.weights:
            self.weightInit()
        if not self.biases:
            self.biasesInit()
    
    def train(self,inputs, targets):
        self.forwardPass(inputs)
        self.targets = targets
        self.error = targets - self.outputs[-1]
        self.backwardPass()
        self.weightsUpdate()
        
            
    def forwardPass(self,inputs):
        self.outputs.append(inputs)
        for i in range(len(self.weights)):
            result = self.weights[i] * self.outputs[-1] + self.biases[i]
            result = self.sigmoid(result)
            self.outputs.append(result)

            
    def backwardPass(self):
        for i in range(self.layers - 1):
            jacobian = self.jacobian(self.outputs[-1-i].shape[0], self.outputs[-1-i])
            self.jacobians_list.append(jacobian)
            if i == 0:
                s = self.jacobians_list[-1] * self.error * -2
            else: 
                rhs = self.weights[-i].T * self.deltas[-1]
                s = self.jacobians_list[-1] * rhs
            self.deltas.append(s)
    
    def predict(self,inputs):
        self.forwardPass(inputs)
        return self.outputs[-1]
            
    def weightsUpdate(self):
        for i in range(self.layers - 1):
            update = self.learning_rate * self.deltas[i] * self.outputs[-2-i].T
            self.weights[-1-i] -= update
            self.biases[-1-i] -= self.learning_rate * self.deltas[i]
    
    def jacobian(self,size, output):
        jacobian = np.zeros((size,size))
        for i in range(size):
            for j in range(size):
                if i == j :
                    jacobian[i,j] = self.sigmoid(output[i],deriv = True)
        return jacobian
            
    def weightInit(self):
        self.weights = []
        for i in range(self.layers - 1):
            self.weights.append(np.random.rand(self.neurons[i+1],self.neurons[i]))
            
    def biasesInit(self):
        self.biases = []
        for i in range(self.layers - 1):
            self.biases.append(np.random.rand(self.neurons[i+1],1))
        
    def sigmoid(self,x, deriv = False):
        if deriv:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))
        
    
neurons = [2,2,2]
inputs = np.matrix([[0.05],[0.10]])
targets = np.matrix([[0.01],[0.99]])
learning_rate = 0.01
NN1 = NeuralNetwork(neurons, learning_rate)
iterations = 1000
for i in range(iterations):
    NN1.train(inputs,targets)
    print("Error:",np.abs(NN1.error.sum()/len(NN1.error)))

