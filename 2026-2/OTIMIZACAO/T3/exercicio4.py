import numpy as np
from scipy import optimize

x1 = 0.001
x2 = 4

def f(x):
    return 2*x + 3/x

xopt = optimize.fminbound(f,x1,x2)

print(xopt)
print(f(xopt))