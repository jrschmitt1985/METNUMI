import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = np.array([1.0, 2.0, 2.5, 3.0, 4.0, 5.0])
y = np.array([0.0, 5.0, 6.5, 7.0, 3.0, 1.0])

n = len(x)

def lagrange(xvalor):
    resultado = 0
    for i in range(n):
        Li = math.prod((xvalor - x[j]) / (x[i] - x[j]) for j in range(n) if j != i)
        resultado += Li * y[i]
    return resultado

xvalor = 3.4
resultado = lagrange(xvalor)

xplot = np.linspace(1, 5, 100)
yplot = [lagrange(xi) for xi in xplot]

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

plt.figure(figsize=(10, 6))
plt.plot(xplot, yplot, 'b-', label='Polinômio de Lagrange')
plt.plot(x, y, 'ro', label='Dados')
plt.scatter(
    xvalor,
    resultado,
    color='black',
    zorder=5,
    s=50,
    label=f'f({xvalor:.1f}) = {resultado:.6f}'.replace('.', ',')
)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinômio de Lagrange')
plt.legend()
plt.grid(True)

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()

print(
    f"O valor de f({xvalor:.1f}) é aproximadamente {resultado:.6f}"
    .replace('.', ',')
)