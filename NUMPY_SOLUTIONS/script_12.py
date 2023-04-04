#python script to to create array from list and print it's dimension,size and byte occupied in memory
import numpy as np
l=[98.73 ,85.72,80.85 ,75.10]
print(f'Original list is : {l}')
listarr=np.array(l)
print(listarr)
print(f'Dimension of array is {listarr.ndim}')
print(f'Size of array is {listarr.size}')
print(f'Bytes occupied by array in memory is {listarr.nbytes}')
