# Problem 115: Implement Batch Normalization for BCHW Input
# Implement a function that performs Batch Normalization on a 4D NumPy array 
# representing a batch of feature maps in the BCHW format (batch, channels, height, width). The function should normalize the input across the batch and spatial dimensions for each channel, then apply scale (gamma) and shift (beta) parameters. Use the provided epsilon value to ensure numerical stability.

import numpy as np

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	
    # Below is wrong, this is computing the mean and variance across the entire batch 
	# X_b = (X - np.mean(X)) / np.sqrt(np.var(X) + epsilon)
	# batch_norm_result = X_b * gamma + beta
	
    # Correction, need to compute mean and variance across the batch, height and width dimension
	# for each channel separately. 
	# Another point is the scaling and shifting parameters should be broadcastable 
	# to the shape of the input X
	
    # BCHW - 0, 1, 2, 3 , AXIS - 0, 2, 3 ACROSS 1 
	x_mean = np.mean(X, axis=(0,2,3), keepdims=True)
	x_var = np.var(X, axis=(0,2,3), keepdims=True)
	X_b = (X - x_mean) / np.sqrt(x_var + epsilon)
	batch_norm_result = X_b * gamma[None,:,None, None] + beta[None,:,None, None]
	return batch_norm_result