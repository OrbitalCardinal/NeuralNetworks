import numpy as np 
import NeuralNetworks as NN 


cero = np.matrix(
    [
        [0],[0],[0],
        [0],[1],[0],
        [0],[1],[0],
        [0],[1],[0],
        [0],[0],[0]
    ]
)
one = np.matrix(
    [
        [1],[1],[0],
        [1],[1],[0],
        [1],[1],[0],
        [1],[1],[0],
        [1],[1],[0]
    ]
)

two = np.matrix(
    [
        [0],[0],[0],
        [1],[1],[0],
        [0],[0],[0],
        [0],[1],[1],
        [0],[0],[0]
    ]
)

three = np.matrix(
    [
        [0],[0],[0],
        [1],[1],[0],
        [0],[0],[0],
        [1],[1],[0],
        [0],[0],[0]
    ]
)

four = np.matrix(
    [
        [0],[1],[0],
        [0],[1],[0],
        [0],[0],[0],
        [1],[1],[0],
        [1],[1],[0]
    ]
)

five = np.matrix(
    [
        [0],[0],[0],
        [0],[1],[1],
        [0],[0],[0],
        [1],[1],[0],
        [0],[0],[0]
    ]
)

six = np.matrix(
    [
        [0],[0],[0],
        [0],[1],[1],
        [0],[0],[0],
        [0],[1],[0],
        [0],[0],[0]
    ]
)

seven = np.matrix(
    [
        [0],[0],[0],
        [1],[1],[0],
        [1],[1],[0],
        [1],[1],[0],
        [1],[1],[0]
    ]
)

eight = np.matrix(
    [
        [0],[0],[0],
        [0],[1],[0],
        [0],[0],[0],
        [0],[1],[0],
        [0],[0],[0]
    ]
)

nine = np.matrix(
    [
        [0],[0],[0],
        [0],[1],[0],
        [0],[0],[0],
        [1],[1],[0],
        [0],[0],[0]
    ]
)

target_cero = np.matrix(
    [
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_one = np.matrix(
    [
        [0],
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_two = np.matrix(
    [
        [0],
        [0],
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_three = np.matrix(
    [
        [0],
        [0],
        [0],
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_four = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [1],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_five = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [0],
        [1],
        [0],
        [0],
        [0],
        [0]
    ]
)

target_six = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [1],
        [0],
        [0],
        [0]
    ]
)

target_seven = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [1],
        [0],
        [0]
    ]
)

target_eight = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [1],
        [0]
    ]
)

target_nine = np.matrix(
    [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [1]
    ]
)
numbers = [cero,one,two,three,four,five,six,seven,eight,nine]
target = [target_cero, target_one, target_two, target_three, target_four, target_five, target_six, target_seven, target_eight, target_nine]
n_len = len(numbers)
neurons = [15,30,30,40,10]
activation = ["sigmoid", "sigmoid", "sigmoid","sigmoid"]
error = "SE"
lr = 0.01

NN1 = NN.NeuralNetwork(neurons, activation, error, lr)
iterations = 10000
for i in range(iterations):
    index = np.random.choice(range(10))
    NN1.train(numbers[index], target[index])
    print("SE:", np.power(NN1.error,2).sum()/len(NN1.error))
    
def predict(input):
    result = NN1.predict(input)
    max_index = 0
    max_value = 0
    for i in range(result.shape[0]):
        if max_value < result[i].item():
            max_value = result[i].item()
            max_index = i
    if max_index == 0:
        print("Cero")
    elif max_index == 1:
        print("One")
    elif max_index == 2:
        print("Two")
    elif max_index == 3:
        print("Three")
    elif max_index == 4:
        print("Four")
    elif max_index == 5:
        print("Five")
    elif max_index == 6:
        print("Six")
    elif max_index == 7:
        print("Seven")
    elif max_index == 8:
        print("Eight")
    elif max_index == 9:
        print("Nine")
    
        
    
    
    