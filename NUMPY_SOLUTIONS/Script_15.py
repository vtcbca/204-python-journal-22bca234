#Write a NumPy program to create a new shape to an array without changing its data.
#First Reshape 3x2
#Second Reshape 2x3
import numpy as np
list=[1,2,3,4,5,6]
arr=np.array(list)
print (f"Array of shape 3×2 :\n {arr.reshape(3, 2)}") 
print (f"Array of shape 2×3 : \n{arr.reshape(2, 3)}")
