import matplotlib.pyplot as plt
from scipy import optimize as opt
import numpy as np

def f(x,y):
    return 2*x**2 + 3*y**2 - 4*x*y - y -3*x

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure()
plt.contour(X, Y, Z, levels=20)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

def fmin(v):
    x = v[0]
    y = v[1]
    return 2*x**2 + 3*y**2 - 4*x*y - y - 3*x

x0 = [0, 0]

resultado = opt.minimize(fmin, x0, method='Nelder-Mead')

xmin = resultado.x[0]
ymin = resultado.x[1]
zmin = resultado.fun

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xmin, ymin, zmin, color='red', s=60)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T(x,y)')



print(resultado.x)
print(resultado.fun)

plt.show()