import math
po = float(input("Enter po [0;pi/2]: "))
p1 = float(input("Enter p1 [0;pi/2]: "))
TOL = 1e-4
No = int(input("No: "))

def funcf(x):
    return x - 0.8 - 0.2*math.sin(x)
def OUTPUT(out):
    print(out)
def secant_method(po, p1, TOL, No):
    i = 2
    qo = funcf(po)
    q1 = funcf(p1)
    while i<= No:
        p = p1 - q1*(p1-po)/(q1-qo)
        OUTPUT(p)
        if abs(p - p1) < TOL:
            print("Result: ")
            OUTPUT(p)
            break
        i = i + 1
        po = p1
        p1 = p
        q1 = funcf(p)
secant_method(po, p1, TOL, No)