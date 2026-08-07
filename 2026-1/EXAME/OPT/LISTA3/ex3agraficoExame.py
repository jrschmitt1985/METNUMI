import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4*x - 1.8*x**2 + 1.2 * x**3 - 0.3*x**4

x = np.linspace (-2,4,100)
y = f(x)

plt.plot(x,y)
plt.grid()
plt.title("Gráfico da função")
plt.xlabel("x")
plt.xlabel("y")
plt.axhline(0, color='black', lw=2)
plt.show()