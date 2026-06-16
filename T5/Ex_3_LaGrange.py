import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.array([0.0, 1.8, 5.0, 6.0, 8.2, 9.2, 12.0])
y = np.array([26.000, 16.415, 5.375, 3.500, 2.015, 2.540, 8.000])

n = len(x)



def lagrange(xvalor):
    resultado = 0
    for i in range(n):
        Li = math.prod((xvalor - x[j]) / (x[i] - x[j]) for j in range(n) if j != i)
        resultado += Li * y[i]
    return resultado


xvalor = 3.5
resultado = lagrange(xvalor)

xplot = np.linspace(0, 12, 500)
yplot = [lagrange(xi) for xi in xplot]

fig, ax = plt.subplots(figsize=(10, 6))



ax.plot(xplot, yplot, 'b-', label='Polinômio de Lagrange')
ax.plot(x, y, 'ro', label='Pontos dados')
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


