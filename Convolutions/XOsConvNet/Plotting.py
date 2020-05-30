import numpy as np
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()
im = ax.imshow(test,cmap="gist_gray")
for i in range(test.shape[0]):
    for j in range(test.shape[1]):
        text = ax.text(j,i,test[i,j],ha="center",va="center",color="r")
plt.show()