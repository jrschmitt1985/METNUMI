
import numpy as np

def f1(x1, x2):
    return x2 + x1**2 - x1 - 0.5

def f2(x1, x2):
    return x2 + 5*x1*x2 - x1**2

def df1_dx1(x1, x2):
    return 2*x1 - 1

def df1_dx2(x1, x2):
    return 1

def df2_dx1(x1, x2):
    return 5*x2 - 2*x1

def df2_dx2(x1, x2):
    return 1 + 5*x1

xold = np.array([1.2, 1.2])

epest = np.array([100.0, 100.0])
eppara = 0.5 * 10**(2-6)
k = 0

while max(epest) >= eppara:

    x1 = xold[0]
    x2 = xold[1]

    det = df1_dx1(x1,x2)*df2_dx2(x1,x2) - df1_dx2(x1,x2)*df2_dx1(x1,x2)

    x1new = x1 - (f1(x1,x2)*df2_dx2(x1,x2) - f2(x1,x2)*df1_dx2(x1,x2))/det

    x2new = x2 - (f2(x1,x2)*df1_dx1(x1,x2) - f1(x1,x2)*df2_dx1(x1,x2))/det

    xnew = np.array([x1new, x2new])

    epest = abs((xnew - xold)/xnew)*100

    xold = xnew.copy()
    k += 1

print("Solução:")
print(xnew)
print("Número de iterações:", k)
print("Erro percentual:", epest)

print("Verificação:")
print("f1 =", f1(xnew[0], xnew[1]))
print("f2 =", f2(xnew[0], xnew[1]))
