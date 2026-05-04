import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(4*x) + np.cos(3*x)

x = np.linspace(0, 2*np.pi, 1000)
y = f(x)

plt.plot(x, y)
plt.title("Gráfico de f(x) = sin(4x) + cos(3x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.axhline(0, color='black', lw=2)
plt.show()