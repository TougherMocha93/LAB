import math

def sigmoid(y): return (1 / (1 + math.exp(y)))
def partS(Y): return(Y * (1 - Y))

alpha = 0.5

x1 = 0.2
x2 = 0.4

w11, w12, w21, w22 = 1, 1, 1, 1
v1, v2 = 1, 1

b1, b2 = 1, 1

t = 0.4
error = 1

def forwardPass():
    global error, Y, v1, v2, w11, w12, w21, w22, b1, b2, H1, H2
    
    h1 = x1 * w11 + x2 * w21
    h2 = x1 * w12 + x2 * w22
    H1, H2 = sigmoid(h1), sigmoid(h2)
    
    y = H1 * v1 + H2 * v2
    Y = sigmoid(y)
    
    error = t - Y

def backwardPass():
    global Y, v1, v2, w11, w12, w21, w22, b1, b2, H1, H2
    
    Dy = error * partS(Y)
    
    DH1 = v1 * Dy * partS(H1)
    DH2 = v2 * Dy * partS(H2)
    
    v1 += alpha * Dy * H1
    v2 += alpha * Dy * H2
    
    w11 += alpha * DH1 * x1
    w12 += alpha * DH2 * x1
    w21 += alpha * DH1 * x2
    w22 += alpha * DH2 * x2
    
    b1 += alpha * DH2
    b2 += alpha * Dy

while error > 0.001:
    forwardPass()
    backwardPass()

print(v1, v2, w11, w12, w21, w22, b1, b2, "\nerror =", error)