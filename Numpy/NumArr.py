import numpy as np

#1D Array
my_arr=np.array([2,5,6,8,3,7])
print("A 1D array in Numpy", my_arr)

#2D Array
my_narr=np.array([[6,3,4,2],[5,6,8,3,7]],dtype=object)
print("A 2D Array in Numpy and will say list but a list in python is an array",my_narr)

#Convert a tuple to an array
tup_to_arr=np.array((2,5,6,8,3,7))
print("Here is the tuple which was transformed to an Array:\n",tup_to_arr)

print("The sum of the first array: ",my_arr.sum())
print("The sum of the tuple: ", tup_to_arr.sum())
