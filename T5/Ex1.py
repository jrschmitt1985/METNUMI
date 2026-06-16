import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter



# Dados do problema
x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50])

y = np.array([-8.00, -6.50, -2.30, -0.50, -0.20, 0.05, 0.10, 0.30, 0.40, 0.30, 0.50, 0.26, 0.90, 3.50, 6.50])

n = len(x)

#Ajuste linear

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
print()


# Ajuste polinomial grau 2

coef2 = np.polyfit(x, y, 2)
y_parabola = np.polyval(coef2, x)

sr_parabola = np.sum((y - y_parabola) ** 2)
syx_parabola = np.sqrt(sr_parabola / (n - 3))
r2_parabola = (st - sr_parabola) / st

print("AJUSTE PARABÓLICO")
print(f"Equação: y = {coef2[0]:.6f}x² + {coef2[1]:.6f}x + {coef2[2]:.6f}")
print(f"Erro padrão da estimativa = {syx_parabola:.6f}")
print(f"Coeficiente de determinação R² = {r2_parabola:.6f}")
print()


# Ajuste polinomial grau 3

coef3 = np.polyfit(x, y, 3)
y_cubica = np.polyval(coef3, x)

sr_cubica = np.sum((y - y_cubica) ** 2)
syx_cubica = np.sqrt(sr_cubica / (n - 4))
r2_cubica = (st - sr_cubica) / st

print("AJUSTE CÚBICO")
print(f"Equação: y = {coef3[0]:.6f}x³ + {coef3[1]:.6f}x² + {coef3[2]:.6f}x + {coef3[3]:.6f}")
print(f"Erro padrão da estimativa = {syx_cubica:.6f}")
print(f"Coeficiente de determinação R² = {r2_cubica:.6f}")
print()


# Gráfico


x_grafico = np.linspace(min(x), max(x), 200)

y_linear_grafico = a0 + a1 * x_grafico
y_parabola_grafico = np.polyval(coef2, x_grafico)
y_cubica_grafico = np.polyval(coef3, x_grafico)

plt.scatter(x, y, label="Dados")
plt.plot(x_grafico, y_linear_grafico, label="Ajuste linear")
plt.plot(x_grafico, y_parabola_grafico, label="Ajuste parabólico")
plt.plot(x_grafico, y_cubica_grafico, label="Ajuste cúbico")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste de Curvas - Problema 1")
plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)


plt.axhline(y=0, color='black', linewidth=1.5)

plt.show()