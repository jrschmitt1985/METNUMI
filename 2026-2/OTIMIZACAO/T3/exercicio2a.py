import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def f(x):
    return -1.5 * x**6 - 2 * x**4 + 12*x



x = np.linspace(0, 2, 100)

virgula = FuncFormatter(lambda valor, pos: f'{valor:.2f}'.replace('.', ','))


plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().xaxis.set_major_formatter(virgula)
plt.grid()
plt.show()