import numpy as np
import matplotlib.pyplot as plt

#Variáveis

n = 10
xi = 2

m = np.linspace(-2.5, 2.5, n)

eppara = 0.5 * (10 ** (2 - n))
epest = 100


def f(xi):
    return ((xi ** 2) - 2)

def df(xi):
    return ((2 * xi))
   

while epest > eppara:
    xnew = xi - (f(xi) / df(xi))
        
    epest = abs((xnew - xi) / xnew) * 100
    xi = xnew

print("Raiz aproxima:", xi)

