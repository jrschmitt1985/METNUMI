import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 400000*(6 - x) + 800000*np.sqrt(x**2 + 4)

i = 6
eppara = 0.5 * (10 ** (2 - i))
epest = 100

x1 = 0
x2 = 3
x3 = 6
iteracoes = 0

while epest >= eppara:
    num = f(x1)*(x2**2 - x3**2) + f(x2)*(x3**2 - x1**2) + f(x3)*(x1**2 - x2**2)
    den = 2*(f(x1)*(x2 - x3) + f(x2)*(x3 - x1) + f(x3)*(x1 - x2))
    x4 = num / den

    if iteracoes > 0:
        epest = abs((x4 - x4_ant) / x4) * 100

    if f(x4) < f(x2):
        x1 = x2
        x2 = x4
    else:
        x3 = x4

    x4_ant = x4
    iteracoes += 1

print(f"P localizado a x = {x4:.6f} km da refinaria")
print(f"Custo mínimo = $ {f(x4):,.2f}")
print(f"Iterações: {iteracoes}")

x_plot = np.linspace(0, 6, 1000)

plt.figure(figsize=(10, 5))
plt.plot(x_plot, f(x_plot), color='black', lw=1.5, label=r'$C(x) = 400000(6-x) + 800000\sqrt{x^2+4}$')
plt.axvline(x4, color='tomato', lw=0.8, ls=':')
plt.plot(x4, f(x4), 'o', color='tomato', markersize=7, label=f'Mínimo: x = {x4:.4f} km')

plt.title('Custo do Oleoduto — Interpolação Quadrática', fontsize=13)
plt.xlabel('x (km)')
plt.ylabel('Custo ($)')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
