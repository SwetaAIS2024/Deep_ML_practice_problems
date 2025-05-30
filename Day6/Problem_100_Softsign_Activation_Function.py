# Implement the Softsign Activation Function

# Implement the Softsign activation function, a smooth activation function used in neural networks. 
# Your task is to compute the Softsign value for a given input, ensuring the output is bounded 
# between -1 and 1.

# formula: Sx = x / (1 + |x|)
import math

def softsign(x: float) -> float:
    val = x / (1 + abs(x))
    return round(val,4)