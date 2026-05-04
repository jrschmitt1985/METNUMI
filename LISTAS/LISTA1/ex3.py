import numpy as np
import math

i = 8
eppara = 0.5 * (10 ** (2-i))
epest = 100

x = 0.3*np.pi

def f(x, n):
    soma = 0
    for i in range(n):
        termo = ((-1)**i * x**(2*i)) / math.factorial(2*i)
        soma += termo
    return soma
print(f"Valor aproximado de cos({x}): {f(x, i):.8f}")