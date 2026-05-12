import numpy as np

A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10,]])

B = np.array([[7.85],
              [-19.3],
              [71.4]
               ])

Xold = np.array(([1],
                 [2],
                 [3]))


Xnew = np.array(([],
                 [],
                 []))

Epest = (abs(Xold-Xnew)/Xold)*100

Eppara = 0.5 * (10**(2-6))

while max(Epest >= Eppara):
    if j < i: 
     a{i,j} * kj - if j>i aij * k-ij)