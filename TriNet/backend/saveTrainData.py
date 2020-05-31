import numpy as np 
import sys
import getData
import string

input = getData.parseRequestData(sys.argv[1], sys.argv[2], "s")
getData.storeData("./backend/trainingData.txt",input,"a")
numero=string.ascii_lowercase.index(sys.argv[3])
regla=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
regla[numero]=1
regla=np.matrix(regla).reshape((len(regla),1))
getData.storeData("./backend/targetData.txt",regla,"a")
print("listo")