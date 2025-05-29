# Dynamic Tanh: Normalization-Free Transformer Activation
# Implement the Dynamic Tanh (DyT) function, a normalization-free transformation inspired
# by the Tanh function. DyT replaces layer normalization in Transformer architectures while 
# preserving squashing behavior and enabling stable training.

import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    # Your code here
    # DyT(x)=γ∗tanh(αx)+β
    dyt = gamma * np.tanh(alpha * x) + beta
    dyt = dyt.tolist()  # Convert numpy array to list
    return dyt