import numpy as np


valor_integral = 879/320   


def f(x):
    return 2 + x**3 - x**4

def f2(x):
    return 6*x - 12*x**2    

a = 0
b = 1.5
xi = (a + b) / 2

truncamento = -1/12 * f2(xi) * (b - a)**3
i = (b - a) * (f(a) + f(b)) / 2

Ept = abs(valor_integral - i) / valor_integral * 100

print("Erro de truncamento estimado (Et) =", truncamento)
print("O valor da integral é: ", i)
print("Erro percentual verdadeiro (Ept) =", Ept, "%")