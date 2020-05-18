import numpy as np 

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

def MSE(target,output):
    return (1/2) * np.power(target - output,2)

def MSE_deriv(target,output):
    return(output - target)

def SE(target,output):
    return np.power(target - output,2)

def SE_deriv(target,output):
    return -2 * (target - output)

def linear(x):
    return x
    
def jacobian(results,n_layers,function):
    jacobian = np.zeros((n_layers,n_layers))
    for i in range(jacobian.shape[0]):
        for j in range(jacobian.shape[1]):
            if function == "sigmoid":
                jacobian[i,j] = sigmoid_deriv(results[i])
            if function == "linear":
                return 1
    return jacobian

inputs = np.array([0.05, 0.10])
# inputs = np.array(1)
targets = np.array([0.01,0.99])
# targets = 1  + np.sin(((np.pi)/4) * inputs)
w1 = np.array([
    [0.15, 0.20],
    [0.25, 0.30]
])
w2 = np.array([
    [0.40, 0.45],
    [0.50,0.55]
])

# w1 = np.array([-0.27, -0.41])
# w2 = np.array([0.09, -0.17])
b1 = 0.35
b2 = 0.60
# b1 = np.array([-0.48, -0.13])
# b2 = 0.48

biases = np.array([b1,b2])
weights = np.array([w1,w2])
results = [inputs.copy()]
layers = 2
#input, hidden, output
neurons = [2,2,2]
layers_activation = ["sigmoid", "sigmoid"]
# layers_activation = ["sigmoid", "linear"]
deltas = []

for i in range(layers):
    if layers_activation[i] == "sigmoid":
        results.append(sigmoid(np.dot(weights[i],results[-1]) + biases[i]))
    elif layers_activation[i] == "linear":
        results.append(linear(np.dot(weights[i],results[-1]) + biases[i]))   

lr = 0.5
print(results)