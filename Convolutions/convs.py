import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2 as cv

# input = Image.open('bird.jpg').convert('L') #PIL IMAGE READ APROACH
#OPENCV IMAGE READ APROACH
input = cv.imread("bird.jpg",0)
input = cv.resize(input,(0,0),fx=0.3,fy=0.3)
input = np.array(input)

#KERNELS
sharpening = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

blur = np.array([
    [0.0625,0.125,0.0625],
    [0.125,0.25,0.125],
    [0.0625,0.125,0.0625]
])

bottom_sobel = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])

emboss = np.array([
    [-2,-1,0],
    [-1,1,1],
    [0,1,2]
])


outline = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

top_sobel = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
])

#FILTERS ARRAY FOR AUTOMATION
filters = np.array([sharpening,blur,bottom_sobel,emboss,outline,top_sobel])
filtersNames = np.array(["sharpening","blur","bottom_sobel","emboss","outline","top_sobel"])

#CONVOLUTION
'''The operation that occurs in a convolution is more accurately described as corss correlation'''
def crossCorr2d(input, kernel,padding = False):
    h,w = kernel.shape
    H,W = input.shape
    pad = 0
    expansion = 0
    '''
    If padding is True then the input matrix is reshaped into a matrix with a border of zeros.
    This is used in case the kernel doesn't fit correctly in the matrix to perform the cross correlation operation.
    Each zeros border represents one extra dimension in the input matrix and since
           there is the top-border bottom-border for dimension X (rows) and left-border right-border for dimension Y (columns)
           the pad is multiplied by two and this can be added to the original dimensions of the input matrix
           Example:
           
            (4,4)     (4+2,4+2)
            Input      Padding
           1 2 3 4   0 0 0 0 0 0
           5 6 7 8   0 1 2 3 4 0
           9 1 5 6   0 5 6 7 8 0
                     0 9 1 5 6 0
                     0 0 0 0 0 0 
    '''
    if(padding):
        pad = h - 1
        expansion = pad * 2 #Two borders of zeros
        paddedInput = np.zeros((H+expansion, W+expansion))
        #Assigning old values in the center of the matrix with padding
        for i in range(input.shape[0]):
            for j in range(input.shape[1]):
                paddedInput[i+pad,j+pad] = input[i,j]
        #Replace the original input with the padded input matrix
        input = paddedInput
    
    '''Output matrix dimensions are determined by 
       Rows: the sum of the rows of the input matrix minus the rows of the kernel matrix + number of borders addded + 1
       columns: the sum of the columns of the input matrix minus the columns of the kernel matrix + number of borders addded + 1
    '''
    output = np.zeros((H-h+expansion+1, W-w+expansion+1))
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i,j] = (input[i:i+h, j:j+w] * kernel).sum()
    return output


def plotKernels(): #Automated convolution plotting for each declared kernel
    #Subplots
    rows = 2
    columns = 3
    fig = plt.figure(figsize=(rows,columns))
    ax = []
    for i in range(len(filters)):
        filteredImg = crossCorr2d(input, filters[i],padding=False)
        ax.append(fig.add_subplot(rows,columns,i+1))
        ax[-1].set_title(filtersNames[i])
        filteredPlot = plt.imshow(filteredImg)
        filteredPlot.set_cmap("gray")

    plt.show()
    
#Test function of convolution
def test():    
    test_matrix = np.array([
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ])

    test_kernel1 = np.array([
        [0,1],
        [2,3]
    ])

    test_kernel2 = np.array([
        [0,1,3],
        [4,5,6],
        [7,8,9]
    ])
    
    test_kernel = test_kernel1
    print("Input")
    print(test_matrix)
    print("Kernel")
    print(test_kernel)
    print("Output")
    test_conv = crossCorr2d(test_matrix,test_kernel,padding=True)
    print(test_conv)

# test()
plotKernels()
