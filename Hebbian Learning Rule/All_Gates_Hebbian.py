x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
B = [1, 1, 1, 1]

def allGates(y):
    dw1, dw2, db = [], [], []
    w1, w2, b = [0], [0], [0]

    for i in range(len(x1)):
        dw1.append(x1[i] * y[i])
        dw2.append(x2[i] * y[i])
        db.append(B[i] * y[i])

        w1.append(w1[i] + dw1[i])
        w2.append(w2[i] + dw2[i])
        b.append(b[i] + db[i])

    print(w1[-1], w2[-1], b[-1])

def notGate(y):
    x1 = [1, -1]
    B = [1, 1]

    dw1, db = [], []
    w1, b = [0], [0]

    for i in range(len(x1)):
        dw1.append(x1[i] * y[i])
        db.append(B[i] * y[i])

        w1.append(w1[i] + dw1[i])
        b.append(b[i] + db[i])

    print(w1[-1], b[-1])

while True:
    gate = input("\nEnter the GATE: ").lower()

    match gate:
        case 'not':
            notGate([-1, 1])
        case 'and':
            allGates([1, -1, -1, -1])
        case 'or':
            allGates([1, 1, 1, -1])
        case 'nand':
            allGates([-1, 1, 1, 1])
        case 'nor':
            allGates([-1, -1, -1, 1])
        case 'xor':
            allGates([-1, 1, 1, -1])
        case 'exit':
            break
        case _:
            print("Enter a valid GATE")

print("Exiting the program.")
