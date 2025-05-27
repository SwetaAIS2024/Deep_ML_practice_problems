# Write a Python function leaky_relu that implements the Leaky Rectified Linear Unit (Leaky ReLU) activation function. 
# The function should take a float z as input and an optional float alpha, with a default value of 0.01, as the slope 
# for negative inputs. The function should return the value after applying the Leaky ReLU function.


def leaky_relu(z, alpha):
    if z > 0:
        result_lr = z
    else:
        result_lr = alpha * z
        
    return result_lr