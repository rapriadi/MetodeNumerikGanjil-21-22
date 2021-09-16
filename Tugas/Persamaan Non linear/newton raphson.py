import numpy as np

def f(x):
    return (x*x) - (2*x)*np.sin(x)

def g(x):
    return (2*x) - 2*np.sin(x) - (2*x)*np.cos(x)

x = np.zeros(20)
x[0] = 10

for n in range(0,10):
    x[n+1]=x[n]-f(x[n])/g(x[n])
    print(x[n], '\t' ,f(x[n]))
    