import math
import statistics

weights = [2, 1]
input_var = [0.5, 0.6]
new_y_array = []
new_x_array = []

def sum_of_products():
    sum = 0
    for i in range(len(weights)):
        sum += weights[i] * input_var[i]
    return sum

def step(y):
    return 1 if y >= 0 else 0

def sign(y):
    return 1 if y >= 0 else -1

def linear(y):
    return y

def ReLU(y):
    return 0 if y < 0 else y

def leaky_ReLU(y, a):
    return (a * y) if y < 0 else y

def hyperbolic_tangent(y):
    return math.tanh(y)

def sigmoid(y):
    return 1 / (1 + math.exp(-y))

def softmax(y_array):
    global new_y_array
    new_y_array = []
    sum_exp = sum(math.exp(y) for y in y_array)
    for y in y_array:
        new_y_array.append(math.exp(y) / sum_exp)

def radial_basis():
    global new_x_array
    new_x_array = []
    mean = statistics.mean(input_var)
    variance = statistics.variance(input_var)
    for x in input_var:
        new_x_array.append(((x - mean) ** 2) / (2 * variance))

print("Select from the below:")
print("1. Step\n2. Sign\n3. Linear\n4. ReLU\n5. Leaky ReLU\n6. Hyperbolic Tangent")
print("7. Sigmoid\n8. Softmax\n9. Radial Basis\n0. Exit")

def main():
    y = sum_of_products()
    func = int(input("\nEnter the function number: "))
    if func == 1:
        print(step(y))
    elif func == 2:
        print(sign(y))
    elif func == 3:
        print(linear(y))
    elif func == 4:
        print(ReLU(y))
    elif func == 5:
        a = float(input("Enter alpha value: "))
        print(leaky_ReLU(y, a))
    elif func == 6:
        print(hyperbolic_tangent(y))
    elif func == 7:
        print(sigmoid(y))
    elif func == 8:
        y_array = list(map(float, input("Enter multiple y values: ").split()))
        softmax(y_array)
        print(new_y_array)
    elif func == 9:
        radial_basis()
        print(new_x_array)
    elif func == 0:
        return

    main()

main()
