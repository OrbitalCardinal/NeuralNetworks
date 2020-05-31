def RELU(matrix):
    new_matrix = matrix.copy()
    new_matrix[new_matrix < 0] = 0
    return new_matrix
