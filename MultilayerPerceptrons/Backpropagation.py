'''Function aproximation multi layer perceptron with backpropagation'''
import numpy as np
def g(p):
    return 1 + np.sin(np.pi/4 * p)

#Training set 
training_set = g(np.arange(-2,2.2,0.2))

def sigmoid(x, deriv = False):
    result = 1 / (1 + np.exp(-x))
    return result
    
def sigmoid_deriv(x):
    return ((1-x) * (x))
    

def linear(x, deriv=False):
    result = x
    if deriv:
        return 1
    return x
    
#Initializing weights and biases
W1 = np.array([-0.27, -0.41])
b1 = np.array([-0.48, -0.13])
W2 = np.array([0.09, -0.17])
b2 = np.array([0.48])

p = 1
#Training
#Watch the sequence of operations
a1 = sigmoid(np.dot(W1,p) + b1)
a2 = linear(np.dot(W2,a1) + b2)
e = g(p) - a2
s2 = -2 * linear(e, deriv=True) * e
s1 = np.array([[sigmoid_deriv(a1[0]),0],[0,sigmoid_deriv(a1[1])]])
s1 = np.dot(s1,W2) #Matr
s1 = s1 * s2 #scalar
lr = 0.1
W2 = W2 - lr*s2*a1
b2 = b2 - lr*s2
W1 = W1 - lr*s1*p
b1 = b1 - lr*s1
print(b1)