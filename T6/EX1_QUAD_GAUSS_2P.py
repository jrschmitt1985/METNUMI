import numpy as np

def f(x):
    return 2 + x**3 - x**4

valor_integral = 879/320   
a = 0
b = 3/2
xd0 = -np.sqrt(1/3)
xd1 = np.sqrt(1/3)

x0 = ((b + a) + (b - a) * xd0) / 2
x1 = ((b + a) + (b - a) * xd1) / 2

                         
i = (b - a) / 2 * (f(x0) + f(x1))
ept = abs(valor_integral - i) / valor_integral * 100


print("O valor da integral é: ", i)
print("Erro percentual verdadeiro (Ept) =", ept, "%")
