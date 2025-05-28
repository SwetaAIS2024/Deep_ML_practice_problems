# Implement the ELU Activation Function
# Implement the ELU (Exponential Linear Unit) activation function, which
# helps mitigate the limitations of ReLU by providing negative outputs for 
# negative inputs. The function should compute the ELU activation value 
# for a given input.


import numpy as np

def elu(x: float, alpha: float = 1.0) -> float:
    if x > 0.0:
        val = float(x) # output is expected to be float 
    else:
        val = float(alpha * (np.exp(x) - 1.0)) # output is expected to be float 
	
    return np.round(val, 4)