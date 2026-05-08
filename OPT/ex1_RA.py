import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 400000*(6 - x) + 800000*np.sqrt(x**2 + 4)

numero_ouro = 1.6180
xl = 0
xu = 6

i = 6
eppara = 0.5 * (10 ** (2 - i))
epest = 100
xopt = (xl + xu) / 2
iteracoes = 0

while epest >= eppara:
    d = (numero_ouro - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    if f(x1) < f(x2):
        xl = x2
        xopt = x1
    else:
        xu = x1
        xopt = x2

    epest = (2 - numero_ouro) * abs((xu - xl) / xopt) * 100
    iteracoes += 1

print(f"P localizado a x = {xopt:.6f} km da refinaria")
print(f"Custo mínimo = $ {f(xopt):,.2f}")
print(f"Iterações: {iteracoes}")

x_plot = np.linspace(0, 6, 1000)

plt.figure(figsize=(10, 5))
plt.plot(x_plot, f(x_plot), color='black', lw=1.5, label=r'$C(x) = 400000(6-x) + 800000\sqrt{x^2+4}$')
plt.axvline(xopt, color='tomato', lw=0.8, ls=':')
plt.plot(xopt, f(xopt), 'o', color='tomato', markersize=7, label=f'Mínimo: x = {xopt:.4f} km')

plt.title('Custo do Oleoduto', fontsize=13)
plt.xlabel('x (km)')
plt.ylabel('Custo ($)')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()