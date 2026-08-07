import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'x' : [2, 4, 6, 7, 10, 11, 14, 17, 20],
    'y' : [4, 5, 6, 8, 8, 10, 12, 17, 20]
}

df = pd.DataFrame(data)

n=len(df['x'])
sum_x = np.sum(df['x'])
sum_y = np.sum(df['y'])

sum_xx = np.sum(df['x']*df['x'])
sum_xy = np.sum(df['x']*df['y'])

A=np.array([[n, sum_x],
            [sum_x, sum_xx]])
b=np.array([sum_y, sum_xy])

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