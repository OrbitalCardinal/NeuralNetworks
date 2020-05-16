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