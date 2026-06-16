import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Dados do problema
x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 
              2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50])

y = np.array([-8.00, -6.50, -2.30, -0.50, -0.20, 0.05, 0.10, 0.30, 
              0.40, 0.30, 0.50, 0.26, 0.90, 3.50, 6.50])

n = len(x)

# Ajuste linear
sx = np.sum(x)
sy = np.sum(y)
sxy = np.sum(x * y)
sx2 = np.sum(x ** 2)

a1 = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
a0 = np.mean(y) - a1 * np.mean(x)

y_linear = a0 + a1 * x

# Erro padrão da estimativa
sr_linear = np.sum((y - y_linear) ** 2)
syx_linear = np.sqrt(sr_linear / (n - 2))

# Coeficiente de correlação
st = np.sum((y - np.mean(y)) ** 2)
r = np.sqrt((st - sr_linear) / st)

print("AJUSTE LINEAR")
print(f"a0 = {a0:.6f}")
print(f"a1 = {a1:.6f}")
print(f"Equação: y = {a0:.6f} + {a1:.6f}x")
print(f"Erro padrão da estimativa = {syx_linear:.6f}")
print(f"Coeficiente de correlação r = {r:.6f}")

# Gráfico
x_grafico = np.linspace(min(x), max(x), 200)
y_linear_grafico = a0 + a1 * x_grafico

plt.scatter(x, y, label="Dados")
plt.plot(x_grafico, y_linear_grafico, label="Ajuste linear")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste Linear - Problema 1")

plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)


plt.plot(x_grafico, y_linear_grafico, color='blue', linewidth=1)

plt.scatter(x, y, color='red', label="Dados")

plt.grid()
plt.show()