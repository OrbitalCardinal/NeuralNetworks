import numpy as np
import sys 
# w1 = np.matrix([1,2,3],[1,2,3],[1,2,3])
# w2 = np.matrix([4,5,6],[4,5,6])
# w3 = np.matrix([1],[2,][3])
# matrix_list = [w1,w2,w3]

# archivo=open("prueba,txt", 'w')
# for k in matrix_list:
#     for i in range(k.shape[0]):
#         for j in range(k.shape[1]):
#             o = str(k[i,j])+' '
#             if j == k.shape[1]-1:
#                 o = str(k[i,j])
#             archivo.write(o)
#         archivo.write('\n')

def parseRequestData(data, n):
    n = int(n)
    parsedData = data.split(" ")
    parsedData = [float(i) for i in parsedData]
    counter = 0
    matrixData = []
    for i in range(n):
        temp_row = []
        for j in range(n):
            temp_row.append(parsedData[counter])
            counter += 1
        matrixData.append(temp_row)
    matrixData = np.asmatrix(matrixData)
    return matrixData