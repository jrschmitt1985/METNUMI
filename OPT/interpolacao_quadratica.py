import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2/10 - 2*np.sin(x)

i = 6
epara = 0.5 * (10 ** (2 - i))
epest = 100

x1 = 0
x2 = 1
x3 = 4
iteracoes = 0

while epest >= epara:
    num = f(x1)*(x2**2 - x3**2) + f(x2)*(x3**2 - x1**2) + f(x3)*(x1**2 - x2**2)
    den = 2*(f(x1)*(x2 - x3) + f(x2)*(x3 - x1) + f(x3)*(x1 - x2))
    x4 = num / den

    if iteracoes > 0:
        epest = abs((x4 - x4_ant) / x4) * 100

    if f(x4) < f(x2):
        x1 = x2
        x2 = x4
    else:
        x3 = x4

    x4_ant = x4
    iteracoes += 1

print(f"xopt = {x4:.6f}")