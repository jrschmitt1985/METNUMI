import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Dados do problema
x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 
              2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50])

y = np.array([-8.00, -6.50, -2.30, -0.50, -0.20, 0.05, 0.10, 0.30, 
              0.40, 0.30, 0.50, 0.26, 0.90, 3.50, 6.50])

n = len(x)

# Soma total dos quadrados
st = np.sum((y - np.mean(y)) ** 2)

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

# Gráfico
x_grafico = np.linspace(min(x), max(x), 200)
y_cubica_grafico = np.polyval(coef3, x_grafico) 

plt.scatter(x, y, label="Dados")
plt.plot(x_grafico, y_cubica_grafico, label="Ajuste cúbico")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste Cúbico - Problema 1")
plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)
plt.scatter(x, y, color='red', label="Dados")
plt.plot(x_grafico, y_cubica_grafico, color='blue', linewidth=1)



plt.show()