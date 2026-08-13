import numpy as np
from scipy import optimize

def f(x):
    return 2*x + 3/x

x_opt = optimize.fminbound(f,0.1,5)

print(x_opt)