import numpy as numpy
w1 = np.matrix([1,2,3],[1,2,3],[1,2,3])
w2 = np.matrix([4,5,6],[4,5,6])
w3 = np.matrix([1],[2,][3])
matrix_list = [w1,w2,w3]

archivo=open("prueba,txt", 'w')
for k in matrix_list:
    for i in range(k.shape[0]):
        for j in range(k.shape[1]):
            o = str(k[i,j])+' '
            if j == k.shape[1]-1:
                o = str(k[i,j])
            archivo.write(o)
        archivo.write('\n')
        archivo.write('\n')