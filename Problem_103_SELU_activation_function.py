# Implement the SELU (Scaled Exponential Linear Unit) activation function, 
# a self-normalizing variant of ELU. 
# Your task is to compute the SELU value for a given input while ensuring numerical stability.

import math

def selu(x: float) -> float:
	"""
	Implements the SELU (Scaled Exponential Linear Unit) activation function.

	Args:
		x: Input value

	Returns:
		SELU activation value
	"""
	alpha = 1.6732632423543772
	scale = 1.0507009873554804
	# Your code here
	if x > 0:
		selu_output = scale * x
	else:
		selu_output = scale * (alpha * (math.exp(x)-1))
	selu_output = round(selu_output, 4)  # Round to 4 decimal places for consistency
	return selu_output

if __name__ == "__main__":
	# Test cases
    print(selu(0))  # Expected output: 0.0
    print(selu(1))  # Expected output: 1.0507
    print(selu(-1))  # Expected output: -0.0507
    print(selu(2))  # Expected output: 2.1014
    print(selu(-2))  # Expected output: -0.1014