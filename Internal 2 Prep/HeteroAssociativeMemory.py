import numpy as np

vectors = [
    (np.array([[1, 1, 0, 0]]), np.array([[1, 0]])),
    (np.array([[0, 1, 0, 0]]), np.array([[1, 0]])),
    (np.array([[0, 0, 1, 1]]), np.array([[0, 1]])),
    (np.array([[0, 0, 1, 0]]), np.array([[0, 1]]))
]

wt = sum([np.dot(s.transpose(), t) for s,t in vectors])

dps = [np.dot(s, wt) for s,_ in vectors]

m = 0
for i in range(4): m = m + 1 if vectors[i][1].all() == dps[i].all() else m

if m == 4: print("We can construct Hetero Associative Memory")
else: print("We cannot construct Hetero Associative Memory")