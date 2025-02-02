import numpy as np

zeros_array = np.zeros((2, 2)) # initialize your numpy value
print(zeros_array)
print(zeros_array.dtype)

# alter the data type of our elements by specifying a type in the dtype field
ones_array = np.ones((2, 2), dtype=int)
print(ones_array)
print(ones_array.dtype)