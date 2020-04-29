import numpy as np 
import matplotlib.pyplot as plt
n = 30

x_training = np.array([0,0,1,1]) #X points for logic gate AND
y_training = np.array([0,1,0,1]) #Y points for logic gate AND
bias = np.array([1,1,1,1]) #BIAS
training_data = np.stack((x_training,y_training, bias), axis = -1) #Training data matrix
training_results = np.array([0,0,0,1]) #Correct results

w = np.random.normal(size=3) #Weight for point x, y and bias

def hardlim(x): #Activation function
    if x < 0:
        return 0
    if x >= 0:
        return 1
        
print("Inital weights:",w)
t = 10
for i in range(t): #Training iterations
    for j in range(len(x_training)): #Weights adjustment process
        guess = hardlim(np.dot(w,training_data[j])) #Predicted value
        if guess != training_results[j]: #Adjustment condition
            print("Adjusting weights")
            w = w + ((training_results[j] - guess) * training_data[j]) #Weights update
print("Final weights:",w)

def testTrainingData(): #Testing 
    c = 0
    for j in range(len(x_training)):
        guess = hardlim(np.dot(w,training_data[j]))
        if guess == training_results[j]:
            c += 1
        print("Predicted:",guess,"Correct:",training_results[j])
    print("Succes rate:",(c/len(training_results)) * 100)
 
testTrainingData()       


x = np.array([i for i in range(-1,3,1)])
'''The decision boundary line is extracted by clearing the resulting equation of rect line with the weigths and biases
w1x + w2y + b = 0, y = -w1x - b  / w2, this results from the assumption that weights vector is always ortogonal to the boundary decision'''
y = ((-w[0] * x) - w[2]) / w[1] #Decision boundary line
#Plotting
plt.plot(x,y)
plt.scatter(x_training, y_training)
plt.axis([-0.5,1.5,-0.5,1.5])
plt.show()