import numpy as np


valor_integral = 879/320   

a = 0
b = 1.5
h = (b - a) / 2

def f(x):
    return 2 + x**3 - x**4

def f1(x):
    return 3*x**2 - 4*x**3   

def f4(x):
    return -24

i = h/3 * (f(a) + 4 * f((a + b) / 2) + f(b))
et = -1/90 * f4((a + b) / 2) * h**5

ept = abs(valor_integral - i) / valor_integral * 100

print("O valor da integral é: ", i)
print("Erro de truncamento estimado (Et) =", et)
print("Erro percentual verdadeiro (Ept) =", ept, "%")

