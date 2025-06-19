# Write a Python function that computes the transpose of a given matrix.
# The transpose of a matrix is obtained by flipping rows and columns.


def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    # Check if the input matrix is empty
    if not a or not a[0]:
        return []
    # Initialize the transposed matrix with the appropriate dimensions
    b = [[] for i in range(len(a[0]))]
    # Iterate through each row and column of the original matrix

    return b