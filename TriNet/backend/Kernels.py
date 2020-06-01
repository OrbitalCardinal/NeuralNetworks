import numpy as np

horizontal_line = np.array([
    [-1,-1,-1],
    [1,1,1],
    [-1,-1,-1]
])

vertical_line = np.array([
    [-1,1,-1],
    [-1,1,-1],
    [-1,1,-1]
])

diagonal_left = np.array([
    [1,-1,-1],
    [-1,1,-1],
    [-1,-1,1]
])

diagonal_right = np.array([
    [-1,-1,1],
    [-1,1,-1],
    [1,-1,-1]
])

cross = np.array([
    [1,-1,1],
    [-1, 1,-1],
    [1,-1, 1]
])

circular = np.array([
    [-1, 1, -1],
    [ 1,-1,  1],
    [-1, 1, -1]
])