import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.array([1.0, 2.0, 3.0, 5.0, 6.0])
y = np.array([7.0, 4.0, 5.5, 40, 82])

xi = np.array([2.0, 3.0, 5.0])
yi = np.array([y[x == p][0] for p in xi])

n = len(xi)

def lagrange(xvalor):
    resultado = 0
    for i in range(n):
        Li = math.prod((xvalor - x[j]) / (xi[i] - xi[j]) for j in range(n) if j != i)
        resultado += Li * yi[i]
    return resultado


xvalor = 4
resultado = lagrange(xvalor)

xplot = np.linspace(0, 12, 500)
yplot = [lagrange(xi) for xi in xplot]

fig, ax = plt.subplots(figsize=(10, 6))



ax.plot(xplot, yplot, 'b-', label='Polinômio de Lagrange')
ax.plot(x, y, 'ro', label='Pontos utilizados')
ax.scatter(xvalor, resultado, color='black', zorder=5, s=50, label=f'f({xvalor}) = {resultado:.6f}'.replace('.', ','))

ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val:.1f}'.replace('.', ',')))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val:.1f}'.replace('.', ',')))





plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

print(f"O valor de f({xvalor}) é aproximadamente {resultado}")


