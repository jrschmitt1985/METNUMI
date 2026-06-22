import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50])

y = np.array([-8.00, -6.50, -2.30, -0.50, -0.20, 0.05, 0.10, 0.30, 0.40, 0.30, 0.50, 0.26, 0.90, 3.50, 6.50])

n = len(x)

st = np.sum((y - np.mean(y)) ** 2)

coef2 = np.polyfit(x, y, 2)
y_parabola = np.polyval(coef2, x)

sr_parabola = np.sum((y - y_parabola) ** 2)
syx_parabola = np.sqrt(sr_parabola / (n - 3))
r2_parabola = (st - sr_parabola) / st

print("AJUSTE PARABÓLICO")
print(f"Equação: y = {coef2[0]:.6f}x² + {coef2[1]:.6f}x + {coef2[2]:.6f}")
print(f"Erro padrão da estimativa = {syx_parabola:.6f}")
print(f"Coeficiente de determinação R² = {r2_parabola:.6f}")

x_grafico = np.linspace(min(x), max(x), 200)
y_parabola_grafico = np.polyval(coef2, x_grafico)

plt.scatter(x, y, color='red', label="Dados")
plt.plot(x_grafico, y_parabola_grafico,
         color='blue',
         linewidth=1.5,
         label="Ajuste parabólico")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste Parabólico - Problema 1")
plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()