def activation(x):
    if x >= theta:
        return 1
    else:
        return -1

def perceptron():
    dw1, dw2, db = [], [], []
    w1, w2, b = [0], [0], [0]
    y = []
    fY = []

    for i in range(4):
        y.append((x1[i] * w1[i]) + (x2[i] * w2[i]) + b[i])
        fY.append(activation(y[i]))
        dw1.append(alpha * x1[i] * t[i])
        dw2.append(alpha * x2[i] * t[i])
        db.append(alpha * B[i] * t[i])

        if fY[i] == t[i]:
            break

        w1.append(w1[i] + dw1[i])
        w2.append(w2[i] + dw2[i])
        b.append(b[i] + db[i])

    print(w1[-1], w2[-1], b[-1])

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
t = [0, 1, 1, 0]

B = [1, 1, 1, 1]

alpha = 0.1
theta = 0

perceptron()