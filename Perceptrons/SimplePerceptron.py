import numpy as np
import matplotlib.pyplot as plt

#Generating training data
n = 50 #number of data points
x = np.random.rand(n) 
y = np.random.rand(n)
data = [[x[i],y[i],int(x[i] > y[i])] for i in range(n)] #[x,y,output]
W = [np.random.rand(),np.random.rand()]

x1 = np.asarray([-2,2])
y1 = (-W[0] * x1)/W[1]
plt.scatter(x,y)
plt.plot(x1,y1)
plt.axis([0,1,0,1])
plt.show()
print("Initial weights:",W)

#step function
def activation_function(x):
    if x >= 0:
        return 1
    else:
        return 0

#Training
lr = 0.1 #learning rate
t = 150 #Number of iterations
#Weights of inputs without bias, boundary line passes through the origin
for i in range(t):
    for j in range(n):
        sum_ = (data[j][0] * W[0]) + (data[j][1] * W[1])
        estimated = activation_function(sum_)
        expected = data[j][2]
        if estimated != expected:
            error = expected - estimated
            W[0] = W[0] + (lr * data[j][0] * error)
            W[1] = W[1] + (lr * data[j][1] * error)

x1 = np.asarray([-2,2])
y1 = (-W[0] * x1)/W[1]
plt.scatter(x,y)
plt.plot(x1,y1)
plt.axis([0,1,0,1])
plt.show()
print("Final weights:",W)

#Testing
x_test = np.random.rand(n)
y_test = np.random.rand(n)
data_test = [[x_test[i],y_test[i],int(x_test[i] > y_test[i])] for i in range(n)]
success_rate = 0
for i in range(n):
    expected = data_test[i][2]
    sum_test = (data_test[i][0] * W[0]) + (data_test[i][1] * W[1])
    estimated = activation_function(sum_test)
    if estimated == expected:
        success_rate += 1
success_rate = success_rate/n
print("Success rate:",success_rate)