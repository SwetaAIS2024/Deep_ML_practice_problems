# In machine learning and statistics, the softmax function is a generalization of the logistic function that 
# converts a vector of scores into probabilities. The log-softmax function is the logarithm of the softmax function, 
# and it is often used for numerical stability when computing the softmax of large numbers.
# Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.

import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # softmax(scores) = (exp(scores_i) / sum(all exp(scores_i)))
    # log_softmax = log(softmax(scores)) = log((exp(scores_i) / sum(all exp(scores_i)))
    # = score_i - log(sum(all exp(scores_i)))
    exp_scores = np.exp(scores)
    sum_exp_scores = np.sum(exp_scores)
    log_sum_exp_scores = np.log(sum_exp_scores)
    result_log_softmax = [(i - log_sum_exp_scores) for i in scores]
    result_log_softmax = np.round(result_log_softmax, 4)
    return result_log_softmax