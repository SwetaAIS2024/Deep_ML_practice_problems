import math
import numpy as np

def sigmoid(x: float) -> float:
    result_s = 1 / (1 + math.exp(-x))
    #result_s = round(result_s, 4)
    return result_s


def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	result_swish = x * sigmoid(x)
	result_swish =  round(result_swish, 4)
	return result_swish
