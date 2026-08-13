import numpy as np
import matplotlib.pyplot as plt
import math

#valor verdadeiro
u = 2.71828182846

#critério de parada
n = 6
Eppara = 0.5*10**(2-n)

print(Eppara)

def serieMclarium(x,n):
    return (x**n)/math.factorial(n)


#Ept = np.abs((u - v)/u)*100
