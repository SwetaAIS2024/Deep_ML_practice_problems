# Transpose of a Matrix

# Write a Python function that computes the transpose of a given matrix.
# Example:
# Input:
# a = [[1,2,3],[4,5,6]]
# Output:
# [[1,4],[2,5],[3,6]]
# Reasoning:
# The transpose of a matrix is obtained by flipping rows and columns.


def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if a:
        print("Input matrix:", a)
        # create an empty list for the transposed matrix
        b = []
        b = [[] for i in range(len(a[0]))]
        for i in range(len(a[0])):
            for j in range(len(a)):
                b[i][j] = a[j][i]
        return b
    
    else:
        return []
    
# Issue with the current code:
# The code initializes the transposed matrix b with empty lists, but it does not 
# allocate space for the elements.
# This will lead to an IndexError when trying to assign values to b[i][j]
# since the inner lists are empty.



# There are two ways to fix this issue:

# 1. Using a nested loop to initialise the transposed matrix with the correct dimensions
def transpose_matrix_2(a: list[list[int|float]]) -> list[list[int|float]]:
    if a:
        print("Input matrix:", a)
        # create an empty list for the transposed matrix
        #b = []
        b = [[[] for i in range(len(a))] for j in range(len(a[0]))]
        for i in range(len(a[0])):
            for j in range(len(a)):
                b[i][j] = a[j][i]
        return b
    
    else:
        return []



# 2. The second method is more concise and uses the list comprehensions 
# to create the transposed matrix directly without needing to initialize it first.

def transpose_matrix_corrected(a: list[list[int|float]]) -> list[list[int|float]]:
    if a:
        print("Input matrix:", a)
        b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
        return b
    
    else:
        return []


    
if __name__ == "__main__":
    # Test cases
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix_2(a))  # Expected output: [[1, 4], [2, 5], [3, 6]]
    # print(transpose_matrix_corrected(a))  # Expected output: [[1, 4], [2, 5], [3, 6]]

    b = [[1, 2], [3, 4], [5, 6]]
    print(transpose_matrix_2(b))  # Expected output: [[1, 3, 5], [2, 4, 6]]
    # print(transpose_matrix_corrected(b))  # Expected output: [[1, 3, 5], [2, 4, 6]]

    c = []
    print(transpose_matrix_2(c))  # Expected output: []
    # print(transpose_matrix_corrected(c))  # Expected output: []