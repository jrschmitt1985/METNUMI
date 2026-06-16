import numpy as np
import math

x = np.array([1.0, 2.0, 2.5, 3.0, 4.0, 5.0])
y = np.array([0.0, 5.0, 6.5, 7.0, 3.0, 1.0])

n = len(x)
c = y.copy()
for j in range(1, n):
    for i in range(n-1, j-1, -1):
        c[i] = (c[i] - c[i-1]) / (x[i] - x[i-j])

xvalor = 3.4
resultado = c[0]
for i in range(1, n):
    resultado += c[i] * math.prod(xvalor - x[k] for k in range(i))

print(f"f({xvalor}) = {resultado:.6f}")