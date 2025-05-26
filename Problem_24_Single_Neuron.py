# Single Neuron implementation
# Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, 
# handling multidimensional input features. The function should take a list of feature vectors (each vector representing 
# multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and b
# ias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between 
# the predicted probabilities and the true labels, both rounded to four decimal places.

import math
import numpy as np

def act_sigmoid(z):
    result = 1 / (1 + np.exp(-z))
    return result

def wtd_sum(features, weights, bias):
    x_dot_w = np.dot(features, weights)
    wtd_sum_result = x_dot_w + bias # broadcast
    return wtd_sum_result

def mse_custom(y_actual, y_pred):
    # Calculate Mean Squared Error
    mse_result = np.mean((y_actual - y_pred)**2)
    return mse_result

def single_neuron_model(features, labels, weights, bias):
	# Your code here
    y_actual = np.array(labels)
    y_hat = wtd_sum(features, weights, bias) # this is an array 
    y_pred = act_sigmoid(y_hat)
    mse_val = mse_custom(y_actual, y_pred)
    
    prob_rounded = np.round(y_pred, 4)
    mse_rounded = np.round(mse_val, 4)
    return prob_rounded, mse_rounded

if __name__ == "__main__":
    # Test cases
    probabilities, mse = single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1)
    #expected output : ([0.4626, 0.4134, 0.6682], 0.3349)
    #my output : Predicted Probabilities: [0.4626 0.4134 0.6682] Mean Squared Error: 0.3349
    print("Predicted Probabilities:", probabilities)  # Expected output: probabilities rounded to 4 decimal places
    print("Mean Squared Error:", mse)  # Expected output: MSE rounded to 4 decimal places