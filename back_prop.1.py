import numpy as np
import math


weights_hidden = [0.4, 0.5, 0.45, 0.55]
biases_hidden = [0.35, 0.60]
weights_output = [0.4, 0.5, 0.45, 0.55]
biases_output = [0.35, 0.60]
weights_input_hidden = [0.15, 0.25, 0.20, 0.30]
biases_input_hidden = [0.35, 0.60]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

def show_activation(value):
    if value <= 0.5:
        return 0
    else:
        return 1
    
def calculate_error():
    global E1, E2
    E1 = t1 - y1f
    E2 = t2 - y2f
    return E1, E2

def forward_pass():
    global y1f, y2f, H1f, H2f
    H1 = x1 * weights_input_hidden[0] + x2 * weights_input_hidden[2] + biases_input_hidden[0]
    H2 = x1 * weights_input_hidden[1] + x2 * weights_input_hidden[3] + biases_input_hidden[1]
    H1f = sigmoid(H1)
    H2f = sigmoid(H2)
    y1 = H1f * weights_hidden[0] + H2f * weights_hidden[2] + biases_hidden[0]
    y2 = H1f * weights_hidden[1] + H2f * weights_hidden[3] + biases_hidden[1]
    y1f = sigmoid(y1)
    y2f = sigmoid(y2)


def backpropagation():
    global dw11, dw12, db2, dv11, dv12, dv21, dv22, db1
    
    E1 = t1 - y1f
    E2 = t2 - y2f
    
    
    sy1 = E1 * sigmoid_derivative(y1f)
    sy2 = E2 * sigmoid_derivative(y2f)

    
    sh1 = (sy1 * weights_hidden[0] + sy2 * weights_hidden[1]) * sigmoid_derivative(H1f)
    sh2 = (sy1 * weights_hidden[2] + sy2 * weights_hidden[3]) * sigmoid_derivative(H2f)

    
    dw11 = sy1 * H1f
    dw12 = sy2 * H2f
    db2 = sy1 + sy2

    
    dv11 = sh1 * x1
    dv12 = sh2 * x1
    dv21 = sh1 * x2
    dv22 = sh2 * x2
    db1 = sh1 + sh2

def update_weights_biases():
    global weights_hidden, biases_hidden, weights_input_hidden, biases_input_hidden
    weights_hidden[0] += a * dw11
    weights_hidden[1] += a * dw12
    biases_hidden[0] += a * db2
    weights_input_hidden[0] += a * dv11
    weights_input_hidden[1] += a * dv12
    weights_input_hidden[2] += a * dv21
    weights_input_hidden[3] += a * dv22
    biases_input_hidden[0] += a * db1

x1, x2 = 0.05, 0.1
t1, t2 = 0.01, 0.99
a = 0.5


def train_network():
    epoch = 0
    error_threshold = 0.001

    while True:
        forward_pass()
        E1, E2 = calculate_error()
        backpropagation()
        update_weights_biases()
        epoch += 1

        if abs(E1) < error_threshold and abs(E2) < error_threshold:
            break

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}: Error E1 = {abs(E1)}, Error E2 = {abs(E2)}")

    print(f"Training complete. Epochs: {epoch}, Final Error E1 = {abs(E1)}, Final Error E2 = {abs(E2)}")

train_network()

print("Updated weights and biases:")
print(f"Hidden Weights: {weights_hidden}, Hidden Biases: {biases_hidden}")
print(f"Input Hidden Weights: {weights_input_hidden}, Input Hidden Biases: {biases_input_hidden}")
print(f"Activation of y1: {(show_activation(y1f))}")
print(f"Activation of y2: {(show_activation(y2f))}")