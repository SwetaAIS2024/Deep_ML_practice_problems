# Sigmoid activation function understanding 
# Write a Python function that computes the output of the sigmoid activation function given an input value z. 
# The function should return the output rounded to four decimal places.

import math

def sigmoid(z: float) -> float:
	#Your code here
    result = 1 / (1 + math.exp(-z))
    result = round(result, 4) #for this question, the output to be rounded to 4 decimal places
    return result


if __name__ == "__main__":
# Test cases    
    print(sigmoid(0)) # Expected output: 0.5
    print(sigmoid(1)) # Expected output: 0.7311
    print(sigmoid(-1)) # Expected output: 0.2689