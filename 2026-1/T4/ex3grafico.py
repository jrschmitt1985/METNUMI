import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x=np.linspace(-2, 2, 1000)

y1 = 0.5 - (x**2) + x
y2 = x**2 / (1+5*x)

y2[np.abs(1 + 5*x) < 0.02] = np.nan

plt.plot(x, y1, label='f1(x1,x2) = 0')
plt.plot(x, y2, label='f2(x1,x2) = 0')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Gráfico das funções f1 e f2')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(-2, 2)
plt.ylim(-2, 2)

formatter = FuncFormatter(lambda x, pos: f'{x:.1f}'.replace('.', ','))

ax = plt.gca()
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.show()      
