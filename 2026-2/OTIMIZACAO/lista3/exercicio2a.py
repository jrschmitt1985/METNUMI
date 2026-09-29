import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -1.5 * x**6 - 2 * x**4 + 12*x


x = np.linspace(0, 2, 100)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()