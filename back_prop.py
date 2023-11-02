import math

weights_hidden = [0.4, 0.5, 0.45, 0.55]
biases_hidden = [0.35, 0.60]
weights_output = [0.4, 0.5, 0.45, 0.55]
biases_output = [0.35, 0.60]
weights_input_hidden = [0.15, 0.25, 0.20, 0.30]
biases_input_hidden = [0.35, 0.60]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def derivative(y):
    return y * (1 - y)

def forward_pass():
    global yf, Hf
    Hf = []
    yf = []

    for i in range(len(weights_input_hidden) // 2):
        H = x[0] * weights_input_hidden[i*2] + x[1] * weights_input_hidden[i*2 + 1] + biases_input_hidden[i]
        Hf.append(sigmoid(H))

    for i in range(len(weights_hidden) // 2):
        y = sum(Hf[j] * weights_hidden[i*2 + j] for j in range(len(Hf))) + biases_hidden[i]
        yf.append(sigmoid(y))

def backpropagation():
    global dw, db, dv
    sy = [t[i] - yf[i] for i in range(len(yf))]

    sh = [0] * len(Hf)
    for i in range(len(Hf)):
        sh[i] = sum(sy[j] * weights_hidden[j*2 + i] for j in range(len(yf))) * derivative(Hf[i])

    dw = [sy[i] * Hf[j] for i in range(len(yf)) for j in range(len(Hf))]
    db = [sum(sy)]

    dv = [sh[i] * x[j] for i in range(len(Hf)) for j in range(len(x))]
    db += [sum(sh)]

def update_weights_biases():
    global weights_hidden, biases_hidden, weights_input_hidden, biases_input_hidden
    for i in range(len(weights_hidden)):
        weights_hidden[i] += a * dw[i]
    biases_hidden[0] += a * db[0]
    for i in range(len(weights_input_hidden)):
        weights_input_hidden[i] += a * dv[i]
    biases_input_hidden[0] += a * db[1]

x = [0.05, 0.1]
t = [0.01, 0.99]
a = 0.5

error_threshold = 0.000000000000001
epoch = 0

while True:
    forward_pass()
    E = 0.5 * sum((t[i] - yf[i]) ** 2 for i in range(len(yf)))

    if E < error_threshold:
        break

    backpropagation()
    update_weights_biases()

    epoch += 1

print("Final weights and biases:")
print(f"Hidden Weights: {weights_hidden}, Hidden Biases: {biases_hidden}")
print(f"Input Hidden Weights: {weights_input_hidden}, Input Hidden Biases: {biases_input_hidden}")
print(f"Total epochs: {epoch}")

#Backpropagation at 1710 EPOCHS using Sigmoid Activation Function