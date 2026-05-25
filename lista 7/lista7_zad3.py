import numpy as np

def heun(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0], y[0] = x0, y0

    for i in range(n):
        k1 = f(x[i], y[i])
        y_tylda = y[i] + h * k1
        k2 = f(x[i] + h, y_tylda)
        y[i+1] = y[i] + (h/2) * (k1 + k2)
        x[i+1] = x[i] + h
    return x, y

def richardson(y_h, y_h2, p):
    return y_h2 + (y_h2 - y_h) / (2**p - 1)

def f(x, y):
    return x + y

def exact2(x):
    return np.exp(x) - x - 1

def richardson_error_estimate(y_h, y_h2, p):
    return np.abs(y_h2 - y_h) / (2**p - 1)


x0, y0 = 0, 0
h = 0.1
n = 10
p = 2  

x1, y1 = heun(f, x0, y0, h, n)
x2, y2 = heun(f, x0, y0, h/2, 2*n)
yR = richardson(y1, y2[::2], p)
y_exact = exact2(x1)


true_error = np.max(np.abs(y2[::2] - y_exact))
est_error = np.max(np.abs(y2[::2] - y1) / (2**p - 1))


print("max błąd rzeczywisty:", true_error)
print("max estymowany błąd:", est_error)
print("stosunek:", true_error / est_error)