import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x1=0
x2=2
x3=6

def f(x):
    return -x**2 + 8*x - 12

x4 = x2 - 1/2 * ((x2-x1)**2 * (f(x2) - f(x3)) - (x2-x3)**2 * (f(x2) - f(x1))) / ((x2-x1) * (f(x2) - f(x3)) - (x2-x3) * (f(x2) - f(x1)))

print(f"Valor aproximado da raiz: {x4:.8f}")
print(f"Valor de f(x4): {f(x4):.8f}")
