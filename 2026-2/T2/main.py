import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from bisseccao import bisseccao
from falsaPosicao import falsaPosicao
from newtonRaphson import newtonRaphson
from secante import secante
from secanteModificado import secanteModificado

def f(x):
    return x**5 - x - 1

def df(x):
    return 5*x**4 - 1

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
    resultado = f"xl = {intervalo[0]:.2f}, xu = {intervalo[1]:.2f}"
    print(resultado.replace(".", ","))

print("Número de raízes detectadas:", len(intervalos))

xl = intervalos[0][0]
xu = intervalos[0][1]

Eppara = 0.000001
delta = 0.000001

xr_bis, Epest_bis, iter_bis = bisseccao(f, xl, xu, Eppara)
xr_fp, Epest_fp, iter_fp = falsaPosicao(f, xl, xu, Eppara)
xr_nr, Epest_nr, iter_nr = newtonRaphson(f, df, xu, Eppara)
xr_sec, Epest_sec, iter_sec = secante(f, xl, xu, Eppara)
xr_sm, Epest_sm, iter_sm = secanteModificado(f, xu, delta, Eppara)

print()
print("Bissecção:")
print(f"xr = {xr_bis:.8f}".replace(".", ","))
print(f"Epest = {Epest_bis:.8f}%".replace(".", ","))
print(f"Iterações = {iter_bis}")

print()
print("Falsa Posição:")
print(f"xr = {xr_fp:.8f}".replace(".", ","))
print(f"Epest = {Epest_fp:.8f}%".replace(".", ","))
print(f"Iterações = {iter_fp}")

print()
print("Newton-Raphson:")
print(f"xr = {xr_nr:.8f}".replace(".", ","))
print(f"Epest = {Epest_nr:.8f}%".replace(".", ","))
print(f"Iterações = {iter_nr}")

print()
print("Secante:")
print(f"xr = {xr_sec:.8f}".replace(".", ","))
print(f"Epest = {Epest_sec:.8f}%".replace(".", ","))
print(f"Iterações = {iter_sec}")

print()
print("Secante Modificado:")
print(f"xr = {xr_sm:.8f}".replace(".", ","))
print(f"Epest = {Epest_sm:.8f}%".replace(".", ","))
print(f"Iterações = {iter_sm}")

x = np.linspace(-3, 3, 1000)
y = f(x)

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