import numpy as np
import matplotlib.pyplot as plt

p = np.array([
    [1,1],
    [1,2],
    [2,-1],
    [2,0],
    [-1,2],
    [-2,1],
    [-1,-1],
    [-2,-2]
])

t = np.array([
    [0,0],
    [0,0],
    [0,1],
    [0,1],
    [1,0],
    [1,0],
    [1,1],
    [1,1]    
])

w = np.array([
    [1,0],
    [0,1]
])

b = np.array([1,1])

def hardlim(x): #Activation function
    res = []
    for i in x:
        if i < 0:
            res.append(0)
        if i >= 0:
            res.append(1)
    return np.array(res)

it = 2
print("Initial weights:\n",w, "\nbias",b)
for i in range(it):
    for j in range(len(p)):
        a = hardlim(np.dot(w,p[j]) + b)
        if not np.all(a == t[j]):
            e = t[j] - a
            w = w + np.reshape(e,(2,1))*p[j] 
            b = b + e
print("Final weights:\n",w, "\nbias",b)

#Decision boundary lines
y1 = np.array([i for i in range(-5,5,1)])
x1 =  np.array([-b[0]/w[0,0] for i in range(len(y1))])

x2 = np.array([i for i in range(-5,5,1)])
y2 = np.array([0 for i in range(len(x2))]) 

   
#Plotting
plt.scatter(p[:2,0],p[:2,1], color="white", edgecolors="black")
plt.scatter(p[2:4,0],p[2:4,1], color="white", edgecolors="black", marker="s")
plt.scatter(p[4:6,0],p[4:6,1], color="black")
plt.scatter(p[6:8,0],p[6:8,1], color="black", marker="s")
plt.axis([-2.5,2.5,-2.5,2.5])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()