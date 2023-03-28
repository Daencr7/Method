import math

def gx(x):
    g = 2*x*math.cos(2*x) - (x+1)*(x+1)
    return g

def output(out):
    print(out)

TOL = pow(10, -5)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
No = int(input("Enter No: "))

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

bisection(No, a, b)
