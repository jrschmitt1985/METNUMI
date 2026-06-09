import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# dados de entrada
date = {
    'x': [0, 2, 4, 6, 9, 11, 12, 15, 17, 19],
    'y': [5, 6, 7, 8, 9, 10, 10, 11, 12, 12]
}

df = pd.DataFrame(date)

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
plt.plot(df['x'], df['y'], 'or', label= 'Dados de entrada')
plt.plot(df['x'], ai[0] + ai[1] * df['x'], '-b', label = 'Ajuste Linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# calculos adicionais
Sr = np.sum((df['y'] - ai[0] - ai[1] * df['x'])**2)
y_media = np.mean(df['y'])
St = np.sum((df['y'] - y_media)**2)
R2 = (St - Sr) / St
print(R2)
