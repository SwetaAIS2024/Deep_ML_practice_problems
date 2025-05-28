# Compute Multi-class Cross-Entropy Loss
# Implement a function that computes the average cross-entropy loss for a batch of predictions
# in a multi-class classification task. Your function should take in a batch of predicted probabilities 
# and one-hot encoded true labels, then return the average cross-entropy loss. Ensure that you handle 
# numerical stability by clipping probabilities by epsilon.



import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    clipped_probs = np.clip(predicted_probs, epsilon, 1-epsilon) # thi is needed to avoid log(0) issues, to ensure numerica stability
    ce_loss = (-1.0) * (np.sum(true_labels * np.log(clipped_probs))/ len(predicted_probs))
    return ce_loss