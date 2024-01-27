import numpy as np

# Create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the index of the maximum value in the array
max_index = np.argmax(arr)
print("Index of maximum value:", max_index)

# Find the index of the minimum value in the array
min_index = np.argmin(arr)
print("Index of minimum value:", min_index)