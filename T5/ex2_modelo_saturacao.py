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

# Modelo de taxa de crescimento da saturação
# y = a*x / (b + x)
#
# Linearização:
# 1/y = (b/a)*(1/x) + 1/a

X_sat = 1 / x
Y_sat = 1 / y

coef_sat = np.polyfit(X_sat, Y_sat, 1)
incl_sat = coef_sat[0]
inter_sat = coef_sat[1]

a_sat = 1 / inter_sat
b_sat = incl_sat * a_sat

y_sat = (a_sat * x) / (b_sat + x)

sr_sat = np.sum((y - y_sat) ** 2)
syx_sat = np.sqrt(sr_sat / (n - 2))
r2_sat = (st - sr_sat) / st

print("MODELO DE TAXA DE CRESCIMENTO DA SATURAÇÃO")
print(f"Equação: y = ({a_sat:.6f}x) / ({b_sat:.6f} + x)")
print(f"Erro padrão da estimativa = {syx_sat:.6f}")
print(f"Coeficiente de determinação R² = {r2_sat:.6f}")

# Gráfico

x_grafico = np.linspace(min(x), max(x), 300)
y_sat_grafico = (a_sat * x_grafico) / (b_sat + x_grafico)

plt.scatter(x, y,
            color='red',
            label="Dados")

plt.plot(x_grafico, y_sat_grafico,
         color='blue',
         linewidth=1.5,
         label="Modelo de crescimento da saturação")

plt.xlabel("Taxa de deformação de cisalhamento, 1/s")
plt.ylabel("Tensão de cisalhamento, N/m²")
plt.title("Modelo de Crescimento da Saturação - Problema 20.56")

plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()