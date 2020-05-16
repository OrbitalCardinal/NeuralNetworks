import numpy as np 
import matplotlib.pyplot as plt

test = np.array([
    [0.77,-0.11,0.11,0.33,0.55,-0.11,0.33],
    [-0.11,1.00,-0.11,0.33,-0.11,0.11,-0.11],
    [0.11,-0.11,1.00,-0.33,0.11,-0.11,0.55],
    [0.33,0.33,-0.33,0.55,-0.33,0.33,0.33],
    [0.55,-0.11,0.11,-0.33,1.00,-0.11,0.11],
    [-0.11,0.11,-0.11,0.33,-0.11,1.00,-0.11],
    [0.33,-0.11,0.55,0.33,0.11,-0.11,0.77]
])

def max_pooling(matrix, size, stride):
    pooled_matrix = np.zeros((size * 2, size * 2))
    movey = 0
    for i in range(pooled_matrix.shape[0]):
        movex = 0
        for j in range(pooled_matrix.shape[1]):
            pooled_matrix[i,j] = (matrix[movey:movey+stride,movex:movex+stride]).max()
            movex += 2
        movey += 2
    return pooled_matrix
    

#print(max_pooling(test,2,2))
# plt.imshow(test,cmap="gray")
# plt.show()

    