import numpy as np
import math

x = np.array([1.0, 2.0, 2.5, 3.0, 4.0, 5.0])
y = np.array([0.0, 5.0, 6.5, 7.0, 3.0, 1.0])

n = len(x)
xvalor = 3.4
resultado = 0

for i in range(n):
    Li = math.prod((xvalor - x[j]) / (x[i] - x[j]) for j in range(n) if j != i)
    resultado += Li * y[i]

print(f"f({xvalor}) = {resultado:.6f}")