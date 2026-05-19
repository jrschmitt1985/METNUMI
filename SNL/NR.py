import numpy as np

def f1(x1,x2):
    return (x1**2) - (x1*x2) - 10

def f2(x1,x2):
    return x2 + (3*x1) * (x2**2) - 57

def df1_dx1(x1,x2):
    return (2*x1) - x2

def df1_dx2(x1,x2):
    return -x1

def df2_dx1(x1,x2):
    return 3*(x2**2)

def df2_dx2(x1,x2):
    return 1 + (6*x1*x2)


x_old = np.array([1.5, 3.5])

epest=np.array([100, 100])

i = 6
eppara = 0.5 * (10 ** (2 - i))

while np.max(epest) >= eppara:
    x1_old = x_old[0]
    x2_old = x_old[1]
    
    x1_new = x1_old - ((f1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - f2(x1_old,x2_old)*df1_dx2(x1_old,x2_old))/(df1_dx1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - df1_dx2(x1_old,x2_old)*df2_dx1(x1_old,x2_old)))

    x2_new = x2_old - ((f2(x1_old,x2_old)*df1_dx1(x1_old,x2_old) - f1(x1_old,x2_old)*df2_dx1(x1_old,x2_old))/(df1_dx1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - df1_dx2(x1_old,x2_old)*df2_dx1(x1_old,x2_old)))
    
    x_new = np.array([x1_new, x2_new])

    epest = np.abs((x_new - x_old)/x_new)*100

    x_old = x_new.copy()

print(x_new)