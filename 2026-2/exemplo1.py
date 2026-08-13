import numpy as np
import matplotlib.pyplot as plt
import math

#dados iniciais
x = 1
n = 6
u = 2.71828182846



Eppara = 0.5*10**(2-n)


#série mclaurin
print(Eppara)

def serieMclarium(x,n):
    return (x**n)/math.factorial(n)


#Ept = np.abs((u - v)/u)*100
