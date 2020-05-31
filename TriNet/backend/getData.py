import numpy as np
import sys 

w1 = np.matrix([[1,2,3],[1,2,3],[1,2,3]])
w2 = np.matrix([[4,5,6],[4,5,6]])
w3 = np.matrix([[1],[2],[3]])
matrix_list = [w1,w2,w3]
def storeData(path, matrix_list, mode):
    if mode == "w":
        file=open(path, mode) #open file and set it write mode
        for e in range(len(matrix_list)): 
            k = matrix_list[e] #each element of the matrix list
            for i in range(k.shape[0]): #number of rows of each matrix
                for j in range(k.shape[1]): #number of columns of each matrix
                    o = str(k[i,j])+',' #txt values formatting
                    if j == k.shape[1]-1: # last value without ","
                        o = str(k[i,j])
                    file.write(o)
                file.write('\n') #line break each row
            file.write('\n') #line break each matrix
        file.close()
    elif mode == "a":
        file=open(path, mode) #open file and set it write mode
        for i in range(matrix_list.shape[0]): #number of rows of each matrix
            for j in range(matrix_list.shape[1]): #number of columns of each matrix
                o = str(matrix_list[i,j])+',' #txt values formatting
                if j == matrix_list.shape[1]-1: # last value without ","
                    o = str(matrix_list[i,j])
                file.write(o)
            file.write('\n') #line break each row
        file.write('\n') #line break each row
        file.close()
        
    
def readData(path):
    file = open(path, "r") #open file and set it to read mode
    formatedData = file.readlines() #store every line of the txt in a list
    rowFormatedData = [] #new list without \n 
    list_size = 0 #matrix list size counter 
    rows = [] #stores number of rows of each element in matrix list
    r_counter = 0 #rows counter 
    for i in range(len(formatedData)):
        lb_remove = formatedData[i].replace("\n","") #removing \n
        if lb_remove != "": #append only non empty strings
            rowFormatedData.append(lb_remove)
            r_counter += 1 #every element before "" is a row
        else: 
            list_size +=1 #every "" means a new matrix
            rows.append(r_counter) #storing the number of rows
            r_counter = 0 # row counter restart for new matrix
            
    parsedRowFormatedData = [] # stores parsed values
    for i in rowFormatedData: # each elements in the previous formatted list
        parsedRow = [] # new parsed row
        for j in i.split(","): # for every value in between ","
            parsedRow.append(float(j)) # parse every value and append it to new parse row list
        parsedRowFormatedData.append(parsedRow) # append new parsed row to parsed values list
    final_list = []
    counter = 0
    for i in rows: # append everything into final matrix list
        temp_matrix = []
        for j in range(i):
            temp_matrix.append(parsedRowFormatedData[counter])
            counter += 1
        final_list.append(np.asmatrix(temp_matrix))
    file.close()  
    return final_list

def readArchitecture(path):
    file = open(path,"r")
    architecture = file.readlines()
    for i in range(len(architecture)):
        architecture[i] = architecture[i].replace("\n","")
    neurons = architecture[0].split(",")
    for i in range(len(neurons)):
        neurons[i] = int(neurons[i])
    activation = architecture[1].split(",")
    error = architecture[2]
    learning_rate = float(architecture[3])
    return neurons, activation, error, learning_rate
    file.close()
    

def parseRequestData(data, n, mode): #Parse request string to numbers
    n = int(n)
    parsedData = data.split(" ")
    parsedData = [[float(i)] for i in parsedData]
    if mode == "s":
        parsedData = np.asmatrix(parsedData)
        return parsedData
    elif mode == "c":    
        counter = 0
        matrixData = []
        for i in range(n):
            temp_row = []
            for j in range(n):
                temp_row.append(parsedData[counter][0])
                counter += 1
            matrixData.append(temp_row)
        matrixData = np.asarray(matrixData)
        return matrixData
    