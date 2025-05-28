# KL Divergence Between Two Normal Distributions
# Task: Implement KL Divergence Between Two Normal Distributions
# Your task is to compute the Kullback-Leibler (KL) divergence between two normal distributions. 
# KL divergence measures how one probability distribution differs from a second, reference probability distribution.
# Write a function kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q) that calculates the KL divergence between two 
# normal distributions, where ( P \sim N(\mu_P, \sigma_P^2) ) and ( Q \sim N(\mu_Q, \sigma_Q^2) ).
# The function should return the KL divergence as a floating-point number.

import numpy as np

# formula: 
# KL(P || Q) = log(sigma_q / sigma_ p) + ((sigma_p**2 + (mu_p - mu_q)**2) / (2 * sigma_q**2)) - 0.5

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    temp_result = np.log(sigma_q / sigma_p) + ((sigma_p**2 + (mu_p - mu_q)**2) / (2 * sigma_q**2)) - 0.5
    #result = np.round(temp_result, 6) - do not need the result to be rounded
    return temp_result
