import numpy as np

def f(x):
    return 2 + x**3 - x**4

valor_integral = 879/320   
a = 0
b = 3/2

xd0 = -np.sqrt(3/5)
xd1 = 0
xd2 = np.sqrt(3/5)

c1 = 5/9
c2 = 8/9
c3 = 5/9

x0 = ((b + a) + (b - a) * xd0) / 2
x1 = ((b + a) + (b - a) * xd1) / 2
x2 = ((b + a) + (b - a) * xd2) / 2

i = (b - a) / 2 * (c1 * f(x0) + c2 * f(x1) + c3 * f(x2))
ept = abs(valor_integral - i) / valor_integral * 100

print("O valor da integral é: ", i)
print("Erro percentual verdadeiro (Ept) =", ept, "%")

