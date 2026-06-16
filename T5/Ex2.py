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

# Modelo exponencial
# y = a * e^(b*x)
# ln(y) = ln(a) + b*x

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
print()

# Modelo potência simples
# y = a * x^b
# ln(y) = ln(a) + b*ln(x)

ln_x = np.log(x)

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
print()

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
print()

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
print()

# Gráfico

x_grafico = np.linspace(min(x), max(x), 300)

y_exp_grafico = a_exp * np.exp(b_exp * x_grafico)
y_pot_grafico = a_pot * x_grafico ** b_pot
y_sat_grafico = (a_sat * x_grafico) / (b_sat + x_grafico)
y_par_grafico = np.polyval(coef_par, x_grafico)

plt.scatter(x, y, label="Dados")
plt.plot(x_grafico, y_exp_grafico, label="Exponencial")
plt.plot(x_grafico, y_pot_grafico, label="Potência simples")
plt.plot(x_grafico, y_sat_grafico, label="Crescimento da saturação")
plt.plot(x_grafico, y_par_grafico, label="Parábola")

plt.xlabel("Taxa de deformação de cisalhamento, 1/s")
plt.ylabel("Tensão de cisalhamento, N/m²")
plt.title("Ajuste de Curvas - Problema 20.56")
plt.grid()
plt.legend()

formatter = FuncFormatter(lambda x, pos: f'{x:.2f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()