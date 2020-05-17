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

test2 = np.array([
    [1,0.3,0.6,0.3],
    [0.3,1,0.3,0.6],
    [0.6,0.3,1,0.1],
    [0.3,0.6,0.1,0.8]
])

# for i in range(test.shape[0]):
#     for j in range(test.shape[1]):
#         ax[-1].text(j,i,test[i,j], ha="center", va="center", color="red")

def max_pooling(matrix, size, stride):
    h,w = matrix.shape
    if h%2!=0:
        h=h+1
    if w%2!=0:
        w=w+1
    pooled_matrix = np.zeros((int(h/2),int(w/2)))
    movey = 0
    for i in range(pooled_matrix.shape[0]):
        movex = 0
        for j in range(pooled_matrix.shape[1]):
            pooled_matrix[i,j] = (matrix[movey:movey+size,movex:movex+size]).max()
            movex += stride
        movey += stride
    return pooled_matrix
    

# test = max_pooling(test2,2,2)
# print(test)
# plt.imshow(test,cmap="gray")
# plt.show()

    