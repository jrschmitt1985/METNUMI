import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = np.array([1.0, 2.0, 2.5, 3.0, 4.0, 5.0])
y = np.array([0.0, 5.0, 6.5, 7.0, 3.0, 1.0])

xi = x
yi = y

n = len(xi)
c = yi.copy()
for j in range(1, n):
    for i in range(n-1, j-1, -1):
        c[i] = (c[i] - c[i-1]) / (xi[i] - xi[i-j])

def newton(xvalor):
    resultado = c[0]
    for i in range(1, n):
        resultado += c[i] * math.prod(xvalor - xi[k] for k in range(i))
    return resultado

xplot = np.linspace(1, 5, 500)
formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

plt.figure(figsize=(10, 6))
plt.plot(xplot, [newton(xp) for xp in xplot], 'b-', label='Grau 5')
plt.plot(x, y, 'ro', label='Pontos dados')
plt.scatter(3.4, newton(3.4), color='black', s=50, label=f'f(3.4) = {newton(3.4):.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Grau 3')
plt.legend()
plt.grid(True)
plt.show()
print(f"Grau 5: f(3.4) = {newton(3.4)}")