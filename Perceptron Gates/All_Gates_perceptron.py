x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t = {
    'and': [1, -1, -1, -1],
    'or': [1, 1, 1, -1],
    'nand': [-1, 1, 1, 1],
    'nor': [-1, -1, -1, 1],
    'xor': [-1, 1, 1, -1],
    'not': [1, -1]
}

B = [1 for _ in range(4)]

w1 = [0 for _ in range(4)]
w2 = [0 for _ in range(4)]
b = [0 for _ in range(4)]

alpha = 1
theta = 1

gate = input("Enter the GATE: ").lower()

match gate:
    case 'and':
        target = t['and']
    case 'or':
        target = t['or']
    case 'nand':
        target = t['nand']
    case 'nor':
        target = t['nor']
    case 'xor':
        target = t['xor']
    case 'not':
        target = t['not']
    case _:
        print("Enter a valid GATE")
        exit()

for i in range(4):
    y = x1[i] * w1[i] + x2[i] * w2[i] + b[i]
    if y >= theta:
        y = 1
    else:
        y = -1
    w1[i] += alpha * (target[i % len(target)] - y) * x1[i]
    w2[i] += alpha * (target[i % len(target)] - y) * x2[i]
    b[i] += alpha * (target[i % len(target)] - y)

print(f"{gate.upper()} Gate Weights (w1): {w1}\n{gate.upper()} Gate Weights (w2): {w2}\n{gate.upper()} Gate Biases (b): {b}")
