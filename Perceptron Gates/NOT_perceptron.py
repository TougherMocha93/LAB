#NOR GATE
x1 = [1,-1]
t = [-1,1] 

r = len(t)

B = [1 for _ in range(r)]

w1 = [0 for _ in range(len(t))]
b = [0 for _ in range(r)]

alpha = 1
theta = 1
for i in range(r):
    w1[i] += alpha*t[i]*x1[i]
    b[i] += alpha*t[i]

print(f"{w1}\n{b}")