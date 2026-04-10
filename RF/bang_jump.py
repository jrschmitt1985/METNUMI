import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.81
cd = 0.25
v = 36
t = 4


m = np.linspace(100, 200, 100)

def bang_jump(m):
    return np.sqrt((g*m)/cd) * np.tanh(
        np.sqrt((g*cd)/m) * t
    ) - v

plt.figure()
plt.plot(m, bang_jump(m), label="Bang Jump")
plt.axhline(0, color='red', linestyle='--') 
plt.xlabel("Mass (kg)")
plt.ylabel("Function Value")
plt.title("Bang Jump Function vs Mass")
plt.grid()
plt.show()
    