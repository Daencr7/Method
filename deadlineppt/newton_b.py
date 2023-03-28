po = float(input("Enter (the value between -3 & -2) po : "))
while po < -3 or po >-2:
    po = float(input("Enter (the value between -3 & -2) po : "))
TOL = 1e-4
No = int(input("Enter No: "))

def funcf(x):
    return x**3 + 3*x**2 - 1
def function_df(x):
    g = 1e-5
    return (funcf(x + g)-funcf(x - g))/(2*g)
def OUTPUT(out):
    print(out)
# a = function_df(5)
def newton_method(po, TOL, No):
    i = 1
    while i <= No:
        p = po - funcf(po)/function_df(po)
        OUTPUT(p)
        if abs(p - po) < TOL:
            print("Result: ")
            OUTPUT(p)
            break
        i = i + 1
        po = p
newton_method(po, TOL, No)
