import numpy as np 

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
