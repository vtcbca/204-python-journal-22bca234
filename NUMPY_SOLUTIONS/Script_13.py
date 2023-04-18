#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
#Also displays dimension, size and memory occupied by it. 
import numpy as np
arr=np.arange(2, 11,dtype=int)
matrix=np.reshape(arr, (3, 3))
print(matrix) 
print(f'Dimension of matrix is {matrix.ndim}')
print(f'Size of matrix is {matrix.size }')
print(f'Memory occupied by matrix in bytes is {matrix.nbytes}')