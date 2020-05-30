import numpy as np 

def sigmoid(x,deriv = False):
    if deriv:
        return x * (1 - x)
    return 1/(1 + np.exp(-x))
    
def linear(x,deriv = False):
    if deriv:
        return 1
    return x
    
def jacobian(neurons, activation,x):
    result = np.zeros((neurons,neurons))
    x_counter = 0
    for i in range(neurons):
        for j in range(neurons):
            if i == j:
                if activation == "sigmoid":
                    result[i,j] = sigmoid(x[x_counter], deriv=True)
                elif activation == "linear":
                    result[i,j] = linear(x[x_counter], deriv=True)
                x_counter += 1
    return result
    
inputs = np.matrix([[0.05],[0.10]])
t = np.matrix([[0.01],[0.99]])
w1 = np.matrix([[0.15,0.20],[0.25,0.30]])
w2= np.matrix([[0.40,0.45],[0.50,0.55]])
b1 = 0.35
b2 = 0.60

# inputs = np.matrix([[1]])
# t = 1 + np.sin((np.pi/4) * inputs)
# w1 = np.matrix([[-0.27],[-0.41]])
# w2 = np.matrix([0.09, -0.17])
# b1 = np.matrix([[-0.48],[-0.13]])
# b2 = np.matrix([[0.48]])
activation = ["sigmoid","sigmoid"] #Layers activatiown function
error_function = "SE" #SE, MSE
n = [2,2] #Number of neurons in layers skipping input layer
m  = 2 #number of layers

deltas = [] #sensitivities
#Putting all together
weights = [w1,w2]
outputs = [inputs]
biases = [b1,b2]
lr = 0.5 #Learning rate
iterations = 2
for it in range(iterations):
    #Forward pass
    for i in range(m):
        if activation[i] == "sigmoid":
            outputs.append(sigmoid(weights[i]*outputs[-1] + biases[i]))
        elif activation[i] == "linear":
            outputs.append(linear(weights[i]*outputs[-1] + biases[i]))
    #Sensivities calculation (deltas)
    print("Error",(t - outputs[-1]))
    for i in range(m):
        temp_jacobian = jacobian(n[-1-i],activation[-1-i],outputs[-1-i])
        if i == 0:
            if error_function == "SE":
                s = -2 * temp_jacobian * (t - outputs[-1-i])
            elif error_function == "MSE":
                s = temp_jacobian * (outputs[-1-i] - t)
        else:
            s = temp_jacobian * weights[i].T * deltas[-1]
        deltas.append(s)
    #Weights update
    for i in range(m):
        weights[m-i-1] -= lr * deltas[i] * outputs[-2-i].T
print(outputs[-1])