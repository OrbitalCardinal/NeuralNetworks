import numpy as np 
import matplotlib.pyplot as plt
import Kernels

def crossCorr2d(input, kernel,padding = False):
    h,w = kernel.shape
    H,W = input.shape
    pad = 0
    expansion = 0
    if(padding):
        pad = 1
        expansion = pad * 2 #Two borders of zeros
        paddedInput = np.zeros((H+expansion, W+expansion))
        #Assigning old values in the center of the matrix with padding
        for i in range(input.shape[0]):
            for j in range(input.shape[1]):
                paddedInput[i+pad,j+pad] = input[i,j]
        #Replace the original input with the padded input matrix
        input = paddedInput
        
    output = np.zeros((H-h+expansion+1, W-w+expansion+1))
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i,j] = (input[i:i+h, j:j+w] * kernel).sum()/(h*w)
    return output

def test_function():
    test = np.array([
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1, 1,-1,-1,-1,-1,-1, 1,-1],
        [-1,-1, 1,-1,-1,-1, 1,-1,-1],
        [-1,-1,-1, 1,-1, 1,-1,-1,-1],
        [-1,-1,-1,-1, 1,-1,-1,-1,-1],
        [-1,-1,-1, 1,-1, 1,-1,-1,-1],
        [-1,-1, 1,-1,-1,-1, 1,-1,-1],
        [-1, 1,-1,-1,-1,-1,-1, 1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ])

    filtered = crossCorr2d(test,Kernels.diagonal_left)

    fig = plt.figure(figsize=(10,5), dpi=100)
    ax = []

    ax.append(fig.add_subplot(1,2,1))
    ax[-1].set_title("Original")
    for i in range(test.shape[0]):
        for j in range(test.shape[1]):
            ax[-1].text(j,i,test[i,j], ha="center", va="center", color="orange")
    plt.imshow(test,cmap="gray")

    ax.append(fig.add_subplot(1,2,2))
    ax[-1].set_title("Filtered")
    for i in range(filtered.shape[0]):
        for j in range(filtered.shape[1]):
            ax[-1].text(j,i,"{:0.2f}".format(filtered[i,j]), ha="center", va="center", color="orange")
    plt.imshow(filtered,cmap="gray")
    plt.show()