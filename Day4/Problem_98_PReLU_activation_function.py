# Implement the PReLU Activation Function
# Implement the PReLU (Parametric ReLU) activation function, 
# a variant of the ReLU activation function that introduces a 
# learnable parameter for negative inputs. Your task is to compute 
# the PReLU activation value for a given input.

def prelu(x: float, alpha: float = 0.25) -> float:
	
    if x > 0:
        val = float(x)
    else:
        val = float(alpha * x)

    return val