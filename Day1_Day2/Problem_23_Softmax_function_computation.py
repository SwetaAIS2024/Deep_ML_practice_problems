# Softmax function computation
# Write a Python function that computes the softmax activation for a given list of scores. 
# The function should return the softmax values as a list, each rounded to four decimal places.

import math

def softmax(scores: list[float]) -> list[float]:

    result = []
    temp = [math.exp(i) for i in scores]
    sum_temp = sum(temp)
    result = [round((j/sum_temp),4) for j in temp]

    return result

if __name__ == "__main__":
    # Test cases
    print(softmax([1, 2, 3])) # Expected output: [0.0900, 0.2447, 0.6652]
    print(softmax([1, 1, 1])) # Expected output: [0.3333, 0.3333, 0.3333]
    print(softmax([10, 20, 30])) # Expected output: [0.0000, 0.0000, 1.0000]