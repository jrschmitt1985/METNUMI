import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4 * x - 1.8 * x**2 + 1.2*x**3 - 0.3*x**4


x = np.linspace(-2, 4, 100)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()