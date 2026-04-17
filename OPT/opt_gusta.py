import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**2/10 - 2*np.sin(x)

numero_ouro = 1.6180
xu = 4
xl = 0

i = 6
epara = 0.5 * (10 ** (2 - i))
epest = 100


while epest >= epara:
    d = (numero_ouro - 1)*(xu - xl)
    x1 = xl + d
    x2 = xu - d

    if f(x1) < f(x2):
        xl = x2
        xopt = x1
    else:
        xu = x1
        xopt = x2

    epest = (2 - numero_ouro) * abs((xu - xl) / xopt) * 100

print(f"{xopt}")