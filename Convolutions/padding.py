import numpy as np

h = np.random.randint(1,10,1)[0]
w = np.random.randint(1,10,1)[0]
matrix = np.round(np.random.rand(h,w) * 10)
print(matrix)
print(matrix.shape)

def padding(matrix,pad):
    h,w = matrix.shape
    expansion = pad * 2
    output = np.zeros((h+expansion,w+expansion))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            output[i+pad,j+pad] = matrix[i,j]
    return output
    
newMatrix = padding(matrix,2)
print(newMatrix)
print(newMatrix.shape)