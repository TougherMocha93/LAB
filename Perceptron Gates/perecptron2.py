x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
B = [1, 1, 1, 1]
_alpha = float(input("Enter 'alpha' value: "))
_theta = float(input("Enter 'theta' value: "))

def activation(y):
  if y > _theta:
    return 1
  elif -_theta <= y <= _theta:
    return 0
  else:
    return -1

def allGates(t):
  dw1, dw2, db = [], [], []
  w1, w2, b = [0], [0], [0]
  y = []
  fY = []

  for i in range(len(x1)):
    y.append((x1[i] * w1[i]) + (x2[i] * w2[i]) + b[i])
    fY.append(activation(y[i]))
    dw1.append(_alpha * x1[i] * t[i])
    dw2.append(_alpha * x2[i] * t[i])
    db.append(_alpha * B[i] * t[i])

    if fY[i] == t[i]: break
    
    w1.append(w1[i] + dw1[i])
    w2.append(w2[i] + dw2[i])
    b.append(b[i] + db[i])

  print(w1[-1], w2[-1], b[-1])

def notGate(t):
  x1 = [1, -1]
  B = [1, 1]

  dw1, db = [], []
  w1, b = [0], [0]
  y = []
  fY = []

  for i in range(len(x1)):
    y.append((x1[i] * w1[i]) + b[i])
    fY.append(activation(y[i]))
    dw1.append(_alpha * x1[i] * t[i])
    db.append(_alpha * B[i] * t[i])

    w1.append(w1[i] + dw1[i])
    b.append(b[i] + db[i])

  print(w1[-1], b[-1])

def conn():
  gate = input("\nEnter the GATE: ").lower()

  if gate == 'not': notGate([-1, 1])
  elif gate == 'and': allGates([1, -1, -1, -1])
  elif gate == 'or': allGates([1, 1, 1, -1])
  elif gate == 'nand': allGates([-1, 1, 1, 1])
  elif gate == 'nor': allGates([-1, -1, -1, 1])
  elif gate == 'xor': allGates([-1, 1, 1, -1])
  elif gate == 'exit': return
  else: print("Enter a valid GATE")

  conn()

conn()