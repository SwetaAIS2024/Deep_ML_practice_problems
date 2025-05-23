# Single Neuron implementation
# Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, 
# handling multidimensional input features. The function should take a list of feature vectors (each vector representing 
# multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and b
# ias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between 
# the predicted probabilities and the true labels, both rounded to four decimal places.

import math
import numpy as np

def sigmoid(z: float) -> float:
	#Your code here
    result = 1 / (1 + math.exp(-z))
    result = round(result, 4) #the output to be rounded to 4 decimal places
    return result

def softmax(scores: list[float]) -> list[float]:
    result = []
    temp = [math.exp(i) for i in scores]
    sum_temp = sum(temp)
    result = [round((j/sum_temp),4) for j in temp]
    return result

def wtd_sum(features: list[list[float]], weights: list[float], bias: float) -> (list[float]):

    temp_sum = features*weights
    wtd_sum_result = temp_sum + bias # broadcast

    return wtd_sum_result

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    y_actual = labels
    y_hat = wtd_sum(features, weights, bias)
    y_pred = sigmoid(y_hat)
    mse = round(math.mse(y_actual, y_pred), 4)
    probabilities = round(y_hat, 4)
	
    return probabilities, mse