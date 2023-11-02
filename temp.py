import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

input_data = np.array([[0.05, 0.10]])
target_output = np.array([[0.01, 0.99]])

weights_hidden = np.array([[0.15, 0.25], [0.20, 0.30]])
biases_hidden = np.array([0.35, 0.60])
weights_output = np.array([[0.40, 0.50], [0.45, 0.55]])
biases_output = np.array([0.35, 0.60])


learning_rate = 0.5
epochs = 10000

for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(input_data, weights_hidden) + biases_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_output) + biases_output
    output = sigmoid(output_layer_input)

    # Backward propagation
    error = target_output - output
    output_error = error * sigmoid_derivative(output)
    hidden_error = output_error.dot(weights_output.T) * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_output += hidden_layer_output.T.dot(output_error) * learning_rate
    biases_output += np.sum(output_error) * learning_rate

    weights_hidden += input_data.T.dot(hidden_error) * learning_rate
    biases_hidden += np.sum(hidden_error) * learning_rate

    if epoch % 1000 == 0:
        print(f"Error at epoch {epoch}: {np.mean(np.abs(error))}")


print("\nOutput after training:")
print(output)
print("\nError after training:")
print(error)
