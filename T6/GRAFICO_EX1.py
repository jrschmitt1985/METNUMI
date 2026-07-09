import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 + x**3 - x**4

a = 0
b = 1.5


x = np.linspace(a, b, 100)
y = f(x)


plt.plot(x, y, label='f(x) = 2 + x^3 - x^4')
plt.fill_between(x, y, alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x) e área sob a curva')
plt.grid()
plt.show()
