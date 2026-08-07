import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

V = 32000

def area(p):
    x, y = p
    z = V / (x * y)
    return x*y + 2*x*z + 2*y*z

chute = [30, 50]

resultado = minimize(area, chute)

x_min, y_min = resultado.x
z_min = V / (x_min * y_min)
area_min = resultado.fun

print(f"x = {x_min:.6f} cm")
print(f"y = {y_min:.6f} cm")
print(f"z = {z_min:.6f} cm")
print(f"Área mínima = {area_min:.6f} cm²")
print(f"Iterações = {resultado.nit}")
print(f"Convergiu? {resultado.success}")


x = np.linspace(10, 80, 100)
y = np.linspace(10, 80, 100)

X, Y = np.meshgrid(x, y)
Z = V / (X * Y)
A = X*Y + 2*X*Z + 2*Y*Z

plt.figure()
plt.contour(X, Y, A, levels=30)
plt.plot(x_min, y_min, 'ro')
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.title("Curvas de nível da área")
plt.colorbar(label="Área (cm²)")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, A, cmap='viridis', alpha=0.8)
ax.scatter(x_min, y_min, area_min, color='red', s=100, edgecolors='black')
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.set_zlabel("Área (cm²)")
ax.set_title("Superfície da área")
plt.show()