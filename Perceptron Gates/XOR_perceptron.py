#XOR GATE
x1 = [1,1,-1,-1]
x2 = [1,-1,1,-1]
t = [-1,1,1,-1] 

r = len(t)

B = [1 for _ in range(r)]

w1 = [0 for _ in range(r)]
w2 = [0 for _ in range(r)]
b = [0 for _ in range(r)]

alpha = 1
theta = 1
for i in range(r):
    w1[i] += alpha*t[i]*x1[i]
    w2[i] += alpha*t[i]*x2[i]
    b[i] += alpha*t[i]

print(f"{w1}\n{w2}\n{b}")