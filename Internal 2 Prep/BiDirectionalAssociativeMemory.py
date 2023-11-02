import numpy as np

p1, revP1 = np.array([-1, 1]), np.array([1, -1])
p2, revP2 = np.array([1, 1]), np.array([-1, -1])

x = [1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1]
y = [1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1]

e = np.array([p1 if bool_val == 1 else revP1 for bool_val in x])
h = np.array([p2 if bool_val == 1 else revP2 for bool_val in y])
  
w = e + h

Y = np.dot(x, w)
Y_rev = np.dot(p1, w.transpose())

if Y.all() == p1.all() and Y_rev.all() == Y.all():
  print("We can construct Bi-directional Associative Memory")
else:
  print("We cannot construct Bi-directional Associative Memory")