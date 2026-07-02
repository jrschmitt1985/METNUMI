import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


x = np.array([50, 70, 90, 110, 130], dtype=float)
y = np.array([6.01, 7.48, 8.59, 9.19, 10.21], dtype=float)

n = len(x)

st = np.sum((y - np.mean(y)) ** 2)

ln_y = np.log(y)

coef_exp = np.polyfit(x, ln_y, 1)
b_exp = coef_exp[0]
ln_a_exp = coef_exp[1]
a_exp = np.exp(ln_a_exp)

y_exp = a_exp * np.exp(b_exp * x)

sr_exp = np.sum((y - y_exp) ** 2)
syx_exp = np.sqrt(sr_exp / (n - 2))
r2_exp = (st - sr_exp) / st

print("MODELO EXPONENCIAL")
print(f"Equação: y = {a_exp:.6f} * e^({b_exp:.6f}x)")
print(f"Erro padrão da estimativa = {syx_exp:.6f}")
print(f"Coeficiente de determinação R² = {r2_exp:.6f}")


x_grafico = np.linspace(min(x), max(x), 300)
y_exp_grafico = a_exp * np.exp(b_exp * x_grafico)

plt.scatter(x, y,
            color='red',
            label="Dados")

plt.plot(x_grafico, y_exp_grafico,
         color='blue',
         linewidth=1.5,
         label="Modelo exponencial")

plt.xlabel("Taxa de deformação de cisalhamento, 1/s")
plt.ylabel("Tensão de cisalhamento, N/m²")
plt.title("Modelo Exponencial - Problema 20.56")

plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()