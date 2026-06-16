import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 1.8, 5.0, 6.0, 8.2, 9.2, 12.0])
y = np.array([26.000, 16.415, 5.375, 3.500, 2.015, 2.540, 8.000])

n = len(x)
grau = 6


A = np.array([[np.sum(x**(i+j)) for j in range(grau)] for i in range(grau)])
b = np.array([np.sum(y * x**i) for i in range(grau)])

ai = np.linalg.solve(A, b)

def polinomio(xvalor):
    return sum(ai[i] * xvalor**i for i in range(grau))

xplot = np.linspace(0, 12, 500)

plt.figure(figsize=(10, 6))
plt.plot(xplot, [polinomio(xi) for xi in xplot], 'b-', label='Mínimos Quadrados')
plt.plot(x, y, 'ro', label='Pontos dados')
plt.scatter(3.5, polinomio(3.5), color='black', s=50, label=f'f(3.5) = {polinomio(3.5):.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mínimos Quadrados Grau')
plt.legend()
plt.grid(True)
plt.show()

print(f"f(3.5) = {polinomio(3.5)}")

Sr = np.sum((y - np.array([polinomio(xi) for xi in x]))**2)
St = np.sum((y - np.mean(y))**2)
R2 = (St - Sr) / St * 100
print(f"R² = {R2:.2f}%")