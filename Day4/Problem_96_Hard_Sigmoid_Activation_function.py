# Implement the Hard Sigmoid activation function, a computationally efficient approximation 
# of the standard sigmoid function. Your function should take a single input value and return
# the corresponding output based on the Hard Sigmoid definition.


# Understanding the Hard Sigmoid Activation Function
# The Hard Sigmoid is a piecewise linear approximation of the sigmoid activation function. It's computationally more efficient than the standard sigmoid function while maintaining similar characteristics. This function is particularly useful in neural networks where computational efficiency is crucial.
# Mathematical Definition

# The Hard Sigmoid function is mathematically defined as:
# HardSigmoid(x)= 0 if x≤−2.5
#                 0.2x+0.5 if −2.5<x<2.5
#                 1 if x≥2.5

def hard_sigmoid(x: float) -> float:
    if x <= -2.5:
        result = 0.0
    elif -2.5 < x < 2.5:
        result = 0.2 * x + 0.5
    else:
        result = 1.0
    return round(result, 4)
	