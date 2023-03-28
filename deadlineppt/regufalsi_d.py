
import math
import numpy
po = float(input("Enter po [0;pi/2]: "))
p1 = float(input("Enter p1 [0;pi/2]: "))
TOL = 1e-4
No = int(input("Enter No: "))
def OUTPUT(out):
    print(out)

def funcf(x):
    return x - 0.8 - 0.2*math.sin(x)

def regufalsi_method(po, p1, TOL, No):    
    while numpy.sign(funcf(po)*funcf(p1)) > 0:
        print("Input agian")
        po = float(input("Enter po: "))
        p1 = float(input("Enter p1: "))
    if numpy.sign(funcf(po)) > 0:
        i = 2
        qo = funcf(po)
        q1 = funcf(p1)
        while i <= No:
            # p = p1 - funcf(p1)*(p1 - po)/(funcf(p1)-funcf(po))
            OUTPUT(p)
            p = p1 - q1*(p1-po)/(q1-qo)
            if abs(p - p1) < TOL:
                print("Result: ")
                OUTPUT(p)
                break
            i = i + 1
            if numpy.sign(funcf(p)) > 0:
                po = p1
                p1 = p
                q1 = funcf(p)#
            elif numpy.sign(funcf(p)) < 0:
                p1 = p
                q1 = funcf(p)#
            else:
                print("ERROR")

    if numpy.sign(funcf(po)) < 0:
        i = 2
        qo = funcf(po)
        q1 = funcf(p1)
        while i <= No:
            p = p1 - q1*(p1-po)/(q1-qo)
            OUTPUT(p)
            if abs(p - p1) < TOL:
                print("Result: ")
                OUTPUT(p)
                break
            i = i + 1
            if numpy.sign(funcf(p)) < 0:  
                po = p1              
                p1 = p
                q1 = funcf(p)#
            elif numpy.sign(funcf(p)) > 0:
                p1 = p       
                q1 = funcf(p)#     
            else:
                print("ERROR")

if __name__ == '__main__':
    regufalsi_method(po, p1, TOL, No)