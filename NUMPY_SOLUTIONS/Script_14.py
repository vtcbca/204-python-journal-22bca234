#NumPy program to get the values and indices of the elements that are bigger than 10 in a given array. 
import numpy as np
list=[[4,9,13],[11,6,9],[4,14,7],]
arr=np.array(list) 
b=np.where(arr>10)
print(f"Indices of array : {b}")
print (f"Elements of array : {arr[b]}")