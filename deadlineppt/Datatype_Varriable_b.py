
import math

def gx(x):
    g = math.exp(x) - x*x + 3*x - 2
    return g

def output(out):
    print(out)

TOL = pow(10, -5)
No = int(input("Enter No: "))
a = int(input("Enter first value a: "))
b = int(input("Enter final value b: "))

def bisection(No, a, b):
    i = 1
    FA = gx(a)
    while i <= No:
        p = a + (b-a)/2
        FP = gx(p)
        output(p)
        if FP == 0 or (b-a)/2 < TOL:
            print("Result: ")
            output(p)
            break
        i = i + 1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    # output(p)


bisection(No, a, b)
