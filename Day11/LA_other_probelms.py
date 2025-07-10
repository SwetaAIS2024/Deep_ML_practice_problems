# 1. Matrix Multiplication
# Hint:
# Check if the number of columns in the first matrix equals the number of rows in the second.
# Use nested loops or numpy.dot for multiplication.
# Return an empty list if dimensions are incompatible.
def mat_mul(a, b):
    row_a = len(a)
    col_a = len(a[0]) if a else 0
    row_b = len(b)
    col_b = len(b[0]) if b else 0

    # Check for valid dimensions
    if (not a) or (not b) or (col_a != row_b):
        return []

    # Initialize result matrix with zeros
    result = [[0 for _ in range(col_b)] for _ in range(row_a)]

    # Matrix multiplication
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                result[i][j] += a[i][k] * b[k][j]
    return result
# 2. Matrix Trace
# Hint:

# Only defined for square matrices.
# Sum the elements where the row and column indices are equal (i.e., a[i][i]).
# 3. Matrix Flatten
# Hint:

# Use a list comprehension to iterate through each row and each element.
# Or use numpy.flatten() or numpy.ravel() and convert to a list.
# 4. Matrix Row/Column Sum
# Hint:

# For row sums: sum each row individually.
# For column sums: sum elements at each column index across all rows.
# numpy.sum with axis=0 or axis=1 can help.
# 5. Matrix Rotation (90 degrees clockwise)
# Hint:

# Transpose the matrix, then reverse each row.
# Or use slicing and zip/list comprehensions.
# 6. Identity Matrix Check
# Hint:

# Check if the matrix is square.
# All diagonal elements should be 1, all off-diagonal elements should be 0.