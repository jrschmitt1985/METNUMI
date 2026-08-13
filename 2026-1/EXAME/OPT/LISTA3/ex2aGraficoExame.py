import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -1.5*x**6-2*x**4+12*x

x = np.linspace(0,2,100)
y= f(x)


plt.plot(x,y)
plt.title("Gráfico de f(x) =  -1,5x^6 - 2x^4 + 12x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.axhline(0, color='black', lw=2)
plt.show()