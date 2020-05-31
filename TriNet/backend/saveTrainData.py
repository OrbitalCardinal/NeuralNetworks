import numpy as np 
import sys
import getData

input = getData.parseRequestData(sys.argv[1], sys.argv[2], "s")
getData.storeData("./backend/trainingData.txt",input,"a")
result =getData.readData("./backend/trainingData.txt") 
print(result[0].shape, result[1].shape)