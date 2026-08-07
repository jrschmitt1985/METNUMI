import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


x = np.array([50, 70, 90, 110, 130], dtype=float)
y = np.array([6.01, 7.48, 8.59, 9.19, 10.21], dtype=float)

n = len(x)

st = np.sum((y - np.mean(y)) ** 2)


ln_x = np.log(x)
ln_y = np.log(y)

coef_pot = np.polyfit(ln_x, ln_y, 1)
b_pot = coef_pot[0]
ln_a_pot = coef_pot[1]
a_pot = np.exp(ln_a_pot)

y_pot = a_pot * x ** b_pot

sr_pot = np.sum((y - y_pot) ** 2)
syx_pot = np.sqrt(sr_pot / (n - 2))
r2_pot = (st - sr_pot) / st

print("MODELO POTÊNCIA SIMPLES")
print(f"Equação: y = {a_pot:.6f} * x^{b_pot:.6f}")
print(f"Erro padrão da estimativa = {syx_pot:.6f}")
print(f"Coeficiente de determinação R² = {r2_pot:.6f}")


x_grafico = np.linspace(min(x), max(x), 300)
y_pot_grafico = a_pot * x_grafico ** b_pot

plt.scatter(x, y,
            color='red',
            label="Dados")

plt.plot(x_grafico, y_pot_grafico,
         color='blue',
         linewidth=1.5,
         label="Modelo potência simples")

plt.xlabel("Taxa de deformação de cisalhamento, 1/s")
plt.ylabel("Tensão de cisalhamento, N/m²")
plt.title("Modelo Potência Simples - Problema 20.56")

plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()