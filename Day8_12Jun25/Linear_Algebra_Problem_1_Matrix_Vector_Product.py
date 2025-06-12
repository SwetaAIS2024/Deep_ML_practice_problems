# Write a Python function that computes the dot product of a matrix and a vector. 
# The function should return a list representing the resulting vector if the 
# operation is valid, or -1 if the matrix and vector dimensions are incompatible. 
# A matrix (a list of lists) can be dotted with a vector (a list) only if the number 
# of columns in the matrix equals the length of the vector. For example, an n x m matrix 
# requires a vector of length m.


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
# Return a list where each element is the dot product of a row of 'a' with 'b'.
# If the number of columns in 'a' does not match the length of 'b', return -1.
    # Check if the no of columns in 'a' matches the length of 'b' 
    if len(a[0]) != len(b):
        return -1
    else:
    # Dot product calculation
        result = []
        for r in a:
            temp_product_row = [r[i] * b[i] for i in range(len(r))] 
            print(f"Row: {r}, Vector: {b}, Product Row: {temp_product_row}")
            # Sum the products for each row
            # and append to the result
            result.append(sum(temp_product_row))
    return result


# My thoughts:

# This approach is iterative and straightforward,
# iterating through each row of the matrix and calculating the dot product with the vector.
# If the dimensions are incompatible, it returns -1.
# This is a simple implementation of matrix-vector multiplication.
# Note: The function assumes that the input matrix 'a' is non-empty and well-formed.
# But it is not efficient for large matrices or vectors,
# as it does not utilize any advanced libraries like NumPy for optimized operations.



# Example usage:
if __name__ == "__main__":
    matrix_ex = [[1,2,1],[3,1,3],[4,1,4]]
    vector_ex = [0,0,1]
    result_matrix_dot = matrix_dot_vector(matrix_ex, vector_ex)
    print(result_matrix_dot)  # Expected output: [1, 3, 4]
