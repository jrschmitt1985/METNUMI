import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2/10 - 2*np.sin(x)

numero_ouro = 1.6180
xu = 4
xl = 0

i = 6
epara = 0.5 * (10 ** (2 - i))
epest = 100
xopt = (xl + xu) / 2

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

print(f"xopt = {xopt:.6f} ")
x_plot = np.linspace(-1, 5, 1000)

plt.figure(figsize=(10, 5))
plt.plot(x_plot, f(x_plot), color='black', lw=1.5, label=r'$f(x) = \frac{x^2}{10} - 2\sin(x)$')
plt.axhline(0, color='gray', lw=0.8, ls='--')
plt.plot(xopt, f(xopt), 'o', color='tomato', markersize=7, label=f'Mínimo: x = {xopt:.4f}')
plt.axvline(xopt, color='tomato', lw=0.8, ls=':')

plt.title(r'$f(x) = \frac{x^2}{10} - 2\sin(x)$', fontsize=13)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

