# Write a Python function that simulates a single neuron with sigmoid activation, 
# and implements backpropagation to update the neuron's weights and bias. 
# The function should take a list of feature vectors, associated true binary labels, 
# initial weights, initial bias, a learning rate, and the number of epochs. 
# The function should update the weights and bias using gradient descent based on the MSE loss, 
# and return the updated weights, bias, and a list of MSE values for each epoch, 
# each rounded to four decimal places.


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
    #y_actual = np.array(labels)
    y_hat = wtd_sum(features, weights, bias) # this is an array 
    y_pred = act_sigmoid(y_hat)
    mse_val = mse_custom(labels, y_pred)
    
    prob_rounded = np.round(y_pred, 4)
    mse_rounded = np.round(mse_val, 4)
    return prob_rounded, mse_rounded

def grad_weight(error, y_pred, features):
    temp_w = 2*error*y_pred*(1-y_pred)
    g_wghts = np.dot(features.T, temp_w) / len(features)
    return g_wghts

def grad_bias(error, y_pred, features):
	g_bias = (2*np.sum(error*y_pred*(1-y_pred))) / len(features) # important - here it should be np.sum 
	return g_bias

def me_custom(y_actual, y_pred):
	me_custom_value = (y_actual - y_pred)
	return me_custom_value

def train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs):
	# Your code here
    temp_weights = initial_weights
    temp_bias = initial_bias
    labels = np.array(labels)
    features = np.array(features)
    mse_list= []
    
    for epoch in range(epochs):
        # Forward pass 
        print(f"Epoch {epoch+1}/{epochs}")
        print("Current Weights:", np.round(temp_weights, 4))
        print("Current Bias:", np.round(temp_bias, 4))
        print("Current Learning Rate:", learning_rate)
        y_pred, mse_values = single_neuron_model(features, labels, temp_weights, temp_bias)
        mse_list.append(mse_values)
        print("Predicted Probabilities:", y_pred)
        print("Mean Squared Error:", mse_values)
        err = me_custom(labels, y_pred)
        gradient_weights = grad_weight(err, y_pred, features)
        gradient_bias = grad_bias(err, y_pred, features)
        temp_weights = temp_weights - learning_rate * gradient_weights
        temp_bias = temp_bias - learning_rate * gradient_bias
    

    updated_weights = np.round(temp_weights, 4)
    updated_bias = np.round(temp_bias, 4)
    # Updated weights and bias after training
    print("Updated Weights:", updated_weights)
    print("Updated Bias:", updated_bias)
    print("Final MSE Values:", mse_list)
    return updated_weights, updated_bias, mse_list

if __name__ == "__main__":
    # Test cases
    updated_weights, updated_bias, mse_values = train_neuron(
        features=[[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]],
        labels=[0, 1, 0],
        initial_weights=[0.7, -0.4],
        initial_bias=-0.1,
        learning_rate=0.01,
        epochs=10
    )
    