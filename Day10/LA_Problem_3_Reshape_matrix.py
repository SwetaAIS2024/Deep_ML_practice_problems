# Reshape Matrix
# Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ]
# Example:
# Input:
# a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
# Output:
# [[1, 2], [3, 4], [5, 6], [7, 8]]
# Reasoning:
# The given matrix is reshaped from 2x4 to 4x2.

import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    # original_shape = (len(a), len(a[0])) if a else (0, 0)
    reshaped_matrix = []
    if a:
        original_shape_constraint = len(a) * len(a[0]) # get the total no of elements
        if new_shape[0] * new_shape[1] == original_shape_constraint: # check if the new shape satisfies the constraint
            reshaped_matrix = np.array(a).reshape(new_shape).tolist()
        
    return reshaped_matrix
    

if __name__ == "__main__":
    # Test cases
    a = [[1, 2, 3], [4, 5, 6]]
    new_shape = (3, 2)
    print(reshape_matrix(a, new_shape))  # Expected output: [[1, 4], [2, 5], [3, 6]]

    b = [[1, 2, 3, 4], [5, 6, 7, 8]]
    new_shape = (4, 2)
    print(reshape_matrix(b, new_shape))  # Expected output: [[1, 2], [3, 4], [5, 6], [7, 8]]

    c = []
    new_shape = (0, 0)
    print(reshape_matrix(c, new_shape))  # Expected output: []