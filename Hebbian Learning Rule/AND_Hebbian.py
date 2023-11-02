x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
w = [-1, 0]
b = 0
alpha = 1

for i in range(4):
    y = x1[i] * w[0] + x2[i] * w[1] + b
    w[0] += alpha * x1[i] * y
    w[1] += alpha * x2[i] * y
    b += alpha * y

print("Updated Weights:", w)
print("Updated Bias:", b)