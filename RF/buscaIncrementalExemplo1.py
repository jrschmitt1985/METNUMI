import numpy as np


def f(x):
    return np.sin(10*x) + np.cos(3*x)

#vetor
n = 100
x = np.linspace(3,6,100)
y = f(x)

print(y)

#alocação de memória

xb = []
nb = 0

# Busca Incremental
for i in range(n-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl)*f(xu) < 0):
        nb += 1
        xb.append([xl,xu])
    if not xb:
        print("Nenhum subintervalo foi encontrado!")

print("xb = ", xb)
print("y = ", f(x))
print("Número de intervalos com raiz" , nb)





"""
m = []

m.append([1,2,3,4])

print("m = ", m)
"""