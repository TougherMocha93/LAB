import numpy as np

v_s = np.array([[1, 1, -1, -1]])
inpV = np.array([1, 1, -1, -1])

def activation_function(i):
  if i > 1: return 1
  elif i == 1: return 0
  else: return -1

trans_v_s = v_s.transpose()
weight_matrix = np.dot(trans_v_s, v_s)

t_array = np.array(list(map(int, input("Enter Error Values: ").split())))
t = np.dot(t_array, weight_matrix)

t_result = np.array([])
for i in range(len(t)): t_result = np.append(t_result, activation_function(t[i]))

if (inpV == t_result).all(): print("We can construct Auto Associative Memory")
else: print("We cannot construct Auto Associative Memory")