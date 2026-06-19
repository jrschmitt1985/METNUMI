import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = np.array([0.0, 1.8, 5.0, 6.0, 8.2, 9.2, 12.0])
y = np.array([26.000, 16.415, 5.375, 3.500, 2.015, 2.540, 8.000])

n = len(x)
c = y.copy()

for j in range(1, n):       
    for i in range(n-1, j-1, -1):
        c[i] = (c[i] - c[i-1]) / (x[i] - x[i-j])


def newton(xvalor):
    resultado = c[0]
    for i in range(1, n):
        resultado += c[i] * math.prod(xvalor - x[k] for k in range(i))
    return resultado


xvalor = 3.5
resultado = newton(xvalor)
xplot = np.linspace(0, 12, 500)
yplot = [newton(xi) for xi in xplot]

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

plt.figure(figsize=(10, 6))
plt.plot(xplot, yplot, 'b-', label='Polinômio de Newton')
plt.plot(x, y, 'ro', label='Dados')
plt.scatter(
    xvalor, resultado,
    color='black',
    zorder=5,
    s=50,
    label=f'f({xvalor:.1f}) = {resultado:.6f}'.replace('.', ',')
)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Newton por Diferenças Divididas')
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