import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from bisseccao import bisseccao

def f(x):
    return x**5 - x - 1

xl = -3
xu = 3
dx = 0.01
x = xl
intervalos = []

while x < xu:
    if f(x) * f(x + dx) < 0:
        intervalos.append((x, x + dx))
    x = x + dx

print("Intervalos com mudança de sinal:")

for intervalo in intervalos:
    print(f"xl = {intervalo[0]:.2f}, xu = {intervalo[1]:.2f}")

print("Número de raízes detectadas:", len(intervalos))

x = np.linspace(-3, 3, 1000)
y = f(x)

Eppara = 0.000001

xr, Epest, iteracao = bisseccao(f, 1.16, 1.17, Eppara)

print()
print("Método da Bissecção:")
print(f"xr = {xr:.8f}".replace(".", ","))
print(f"Epest = {Epest:.8f}%".replace(".", ","))
print(f"Iterações = {iteracao}")


plt.figure()
plt.plot(x, y, label="f(x)")
plt.axhline(0, linestyle="--")
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = x⁵ - x - 1")
plt.grid()
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:g}".replace(".", ",")))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f"{y:g}".replace(".", ",")))

plt.show()