import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# dados de entrada
date = {
    'x': [10, 20, 30, 40, 50, 60, 70, 80],
    'y': [28, 70, 380, 550, 610, 1220, 830, 1450]
}

df = pd.DataFrame(date)

df['x'] = np.log10(df['x'])
df['y'] = np.log10(df['y'])

# calculos
n = len(df['x'])
sum_x = np.sum(df['x'])
sum_y = np.sum(df['y'])

sum_xx = np.sum(df['x']*df['x'])
sum_xy = np.sum(df['x']*df['y'])

# construindo as matrizes
A = np.array([[n, sum_x],
              [sum_x, sum_xx]])

b = np.array([sum_y, sum_xy])

# solução do sistema linerar
ai = np.linalg.solve(A,b)

# grafico 
plt.plot(df['x'], (df['y']), 'or', label= 'Dados de entrada')
plt.plot(df['x'], ai[0] + ai[1] * df['x'], '-b', label = 'Ajuste Linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# calculos adicionais
Sr = np.sum((df['y'] - ai[0] - ai[1] * df['x'])**2)
y_media = np.mean(df['y'])
St = np.sum((df['y'] - y_media)**2)
R2 = (St - Sr) / St * 100
print(f"R²: {R2}%")
