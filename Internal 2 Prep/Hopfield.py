import math

def sigmoid(y):
    return 1 / (1 + math.exp(-y))

alpha = 0.5
patterns = [[1, 1, -1, -1], [-1, -1, 1, 1]]

weights = [[0 for _ in range(len(patterns[0]))] for _ in range(len(patterns[0]))]
for pattern in patterns:
    for i in range(len(pattern)):
        for j in range(len(pattern)):
            if i != j:
                weights[i][j] += pattern[i] * pattern[j]

def recall(input_pattern):
    global weights
    output = [0 for _ in range(len(input_pattern))]
    for i in range(len(input_pattern)):
        total = 0
        for j in range(len(input_pattern)):
            total += weights[i][j] * input_pattern[j]
        output[i] = 1 / (1 + math.exp(-total))
    return output

input_pattern = [1, 1, -1, 0]

output_pattern = recall(input_pattern)

print(output_pattern)