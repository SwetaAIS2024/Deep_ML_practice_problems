# Implement the Softplus Activation Function
# Implement the Softplus activation function, a smooth approximation of the ReLU function. 
# Your task is to compute the Softplus value for a given input, handling edge cases to prevent 
# numerical overflow or underflow.

# example - For x = 2, the Softplus activation is calculated as log⁡(1+ex)log(1+ex).

import math

def softplus(x: float) -> float:
	"""
	Compute the softplus activation function.

	Args:
		x: Input value

	Returns:
		The softplus value: log(1 + e^x)
	"""
	val = math.log(1 + math.exp(-math.fabs(x))) + max(0, x)
	
	return round(val,4)


if __name__ == "__main__":
	print(softplus(1000000)) # TCs for large positive input 
	print(softplus(-1000000)) # TCs for large negative input 
	print(softplus(1/1000000)) # TCs for very small positive input 
	print(softplus(-1/1000000)) # TCs for very small negative input 