import sys
from time import sleep
nodeInput = sys.argv[1].split(" ")
nodeInput = [int(i) for i in nodeInput[0:len(nodeInput)-1]]
print([i*2 for i in nodeInput])
    