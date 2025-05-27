# Implement a function that creates a simple residual block using NumPy. 
# The block should take a 1D input array, process it through two weight layers 
# (using matrix multiplication), apply ReLU activations, and add the original input 
# via a shortcut connection before a final ReLU activation.

import numpy as np

def relu(z):
	if z > 0:
		return z
	else:
		return 0
	

def residual_block(input_arr, wght1, wght2):
	expected_size=1
	res_blk_out = 0
	if input_arr.ndim != expected_size:
		print("Input must be a 1D array.")
		return None
	else:
		wght1_output = np.dot(input_arr, wght1)
		print("wght1_output:", wght1_output)
		wght2_output = np.dot(wght1_output, wght2)
		print("wght2_output:", wght2_output)
		relu_output1 = [relu(x) for x in wght2_output]
		print("relu_output1:", relu_output1)
		temp_val = relu_output1 + input_arr
		print("temp_val (after adding input):", temp_val)
		res_blk_out = [relu(y) for y in temp_val]
		print("res_blk_out (final output):", res_blk_out)
	return res_blk_out


if __name__=="__main__":
	# Example usage
    x = np.array([1.0, 2.0])
    w1 = np.array([[1.0, 0.0], [0.0, 1.0]])
    w2 = np.array([[0.5, 0.0], [0.0, 0.5]])
    print(residual_block(x, w1, w2))
    