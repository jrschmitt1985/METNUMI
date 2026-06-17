import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Dados do problema 20.56 - Chapra
# x = taxa de deformação de cisalhamento
# y = tensão de cisalhamento

x = np.array([50, 70, 90, 110, 130], dtype=float)
y = np.array([6.01, 7.48, 8.59, 9.19, 10.21], dtype=float)

n = len(x)

# Soma total dos quadrados
st = np.sum((y - np.mean(y)) ** 2)

# Modelo parabólico
# y = a2*x² + a1*x + a0

coef_par = np.polyfit(x, y, 2)
y_par = np.polyval(coef_par, x)

sr_par = np.sum((y - y_par) ** 2)
syx_par = np.sqrt(sr_par / (n - 3))
r2_par = (st - sr_par) / st

print("MODELO PARABÓLICO")
print(f"Equação: y = {coef_par[0]:.6f}x² + {coef_par[1]:.6f}x + {coef_par[2]:.6f}")
print(f"Erro padrão da estimativa = {syx_par:.6f}")
print(f"Coeficiente de determinação R² = {r2_par:.6f}")

# Gráfico

x_grafico = np.linspace(min(x), max(x), 300)
y_par_grafico = np.polyval(coef_par, x_grafico)

plt.scatter(x, y,
            color='red',
            label="Dados")

plt.plot(x_grafico, y_par_grafico,
         color='blue',
         linewidth=1.5,
         label="Modelo parabólico")

plt.xlabel("Taxa de deformação de cisalhamento, 1/s")
plt.ylabel("Tensão de cisalhamento, N/m²")
plt.title("Modelo Parabólico - Problema 20.56")

plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()