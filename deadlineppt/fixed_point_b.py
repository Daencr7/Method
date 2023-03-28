import math
def gx(x):
    g = 5/(x*x)+2
    return g

def output(out):
    print(out)

po = float(input("Enter po: "))
TOL = 1e-5
No = int(input("Enter No: "))

def fixed_point(po, TOL, No):
    i = 0
    while i <= No:
        p = gx(po)
        output(p)
        if abs(p-po) < TOL:
            print("Result: ")
            output(p)
            break
        i = i + 1
        po = p

fixed_point(po, TOL, No)
