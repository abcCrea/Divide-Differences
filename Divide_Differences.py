# <abc Crea 2020> - <Oscar Eduardo Ochoa Velasco>

import sys

#Declaring the main menu
menu = """
1.- Progressive Difference Method
2.- Regressive Difference Method
3.- Lagrange Form
0.- Exit
"""

#Function that find the interpolate Newton polynomial with the progressive difference method
def Progressive(x,y,f,U):
    #Formula replacing the x since the begin
    p1 = y[0] + (f[0] * (U - x[0]))
    p2 = f[3] * (U - x[0]) * (U - x[1])
    p3 = f[5] * (U - x[0]) * (U - x[1]) * (U - x[2])
    pT = p1 + p2 + p3
    print("")
    #Manual formula sorting the common terms
    x3 = f[5]
    x2 = f[3] + (f[5]*-x[1]) + (f[5]*-x[0]) + (f[5]*-x[2]) 
    x1 = (y[0] + f[0]) + (f[3]*-x[1]) + (f[3]*-x[0]) + (f[5]*-x[1]*-x[2]) + (f[5]*-x[1]*-x[0]) + (f[5]*-x[2]*-x[0])
    xn = (y[0]+(f[0]*-x[0])) + ((f[3]*-x[0]) * -x[1]) + (f[5]*-x[0]*-x[1]*x[2])
    #Printing of the polynomial
    print("P3(x) =",x3,"x^3","+",x2,"x^2","+",x1,"x","+",xn)
    pT = (x3*pow(U,3)) + (x2*pow(U,2)) + (x1*U) + xn
    print("P(", U, ") =", pT)

#Fucntion that find the interpolate Newton polynomial with the regressive difference method
def Regressive(x,y,f,U):
    #Formula replacing the x since the begin
    p1 = y[3] + (f[2] * (U - x[3]))
    p2 = f[4] * (U - x[3]) * (U - x[2])
    p3 = f[5] * (U - x[3]) * (U - x[2]) * (U - x[1])
    pT = p1 + p2 + p3
    print("")
    #Manual formula sorting the common terms
    x3 = f[5]
    x2 = f[4] + (f[5]*-x[1]) + (f[5]*-x[2]) + (f[5]*-x[3]) 
    x1 = (y[3] + f[2]) + (f[4]*-x[2]) + (f[4]*-x[3]) + (f[5]*-x[1]*-x[2]) + (f[5]*-x[1]*-x[3]) + (f[5]*-x[2]*-x[3])
    xn = (y[3]+(f[2]*-x[3])) + ((f[4]*-x[3]) * -x[2]) + (f[5]*-x[3]*-x[1]*x[2])
    #Printing of the polynomial
    print("P3(x) =",x3,"x^3","+",x2,"x^2","+",x1,"x","+",xn)
    pT = (x3*pow(U,3)) + (x2*pow(U,2)) + (x1*U) + xn
    print("P(", U, ") =", pT)

#Function that find the interpolates between the problem intervals
def Divide(x,y,f,U):
    print("Find the value of", U)
    for i in range(4):
        print("If ", x[i], " = ", y[i])
    f[0] = (y[1] - y[0]) / (x[1] - x[0])
    f[1] = (y[2] - y[1]) / (x[2] - x[1])
    f[2] = (y[3] - y[2]) / (x[3] - x[2])
    f[3] = (f[1] - f[0]) / (x[2] - x[0])
    f[4] = (f[2] - f[1]) / (x[3] - x[1])
    f[5] = (f[4] - f[3]) / (x[3] - x[0])
    print("")
    print("f(xi + 1): ")
    for i in range(6):
        print(f[i])

#Function that find the Lagrange form polynomial and the x value with the Lagrange method
def Lagrange(x,y,a,U):
    print("Lagrange Form")
    print("Find the value of", U)
    for i in range(4):
        print("If ", x[i], " = ", y[i])
    a[0] = ((U - x[1])*(U - x[2])*(U-x[3]) * y[0]) / ((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))
    a[1] = ((U - x[0])*(U - x[2])*(U-x[3]) * y[1]) / ((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3]))
    a[2] = ((U - x[0])*(U - x[1])*(U-x[3]) * y[2]) / ((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3]))
    a[3] = ((U - x[0])*(U - x[1])*(U-x[2]) * y[3]) / ((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2]))
    print("")
    print("a(x - x1/x0 - x1): ")
    for i in range(4):
        print(a[i])
    print("")
    pT = a[0] + a[1] + a[2] + a[3]
    print("P3(",U,") =",a[0], "+", a[1], "+", a[2], "+", a[3])
    print("P(", U, ") =", pT)

#Modifiable Variables
x = [0.6,0.7,0.8,1.0]
y = [-0.17694460,0.01375227,0.22363362,0.65809197]
U = 0.9

f = [0,0,0,0,0,0]
a = [0,0,0,0]


print("Interpolate divide differences of Newton")
while True:
    print(menu)
    opc = int(input())
    try: 
        if opc is 1:
            Divide(x,y,f,U)
            Progressive(x,y,f,U)
        elif opc is 2:
            Divide(x,y,f,U)
            Regressive(x,y,f,U)
        elif opc is 3:
            Lagrange(x,y,a,U)
        elif opc is 0:
            sys.exit()
    except ValueError:
        print("ERROR!! Enter only numbers")
