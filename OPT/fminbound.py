from scipy import optimize
import numpy as np

def f(x):
    return (x**2)/10-2*np.sin(x)

xopt = optimize.fminbound(f,0,4)

print(xopt)