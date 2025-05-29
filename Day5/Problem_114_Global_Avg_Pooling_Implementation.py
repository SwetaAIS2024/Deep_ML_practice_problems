# Implement Global Average Pooling

# Implement a function that performs Global Average Pooling on a 3D NumPy array representing feature
# maps from a convolutional layer. The function should take an input of shape (height, width, channels) 
# and return a 1D array of shape (channels,), where each element is the average of all values in the 
# corresponding feature map.


import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	gap = x.mean(axis=(0,1))
	return gap

if __name__ == "__main__":
	x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
	print(global_avg_pool(x))
	xy = np.array([[[100, 200]]])
	print(global_avg_pool(xy))