import numpy as np

valor_integral = 879/320

a = 0
b = 1.5

def f(x):
    return 2 + x**3 - x**4

def f4(x):
    return -24

h = (b - a) / 3

i = 3*h/8 * (f(a) + 3*f(a + h) + 3*f((a + 2*h)) + f(b))

erro = -3/80 * f4((a + b) / 2) * h**5
ept = abs(valor_integral - i) / valor_integral * 100


print("O valor da integral é: ", i)
print("Erro percentual verdadeiro (Ept) =", ept, "%")
print("Erro de truncamento estimado (Et) =", erro)
