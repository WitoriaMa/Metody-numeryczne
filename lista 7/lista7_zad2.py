import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0], y[0] = x0, y0

    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
        x[i+1] = x[i] + h
    return x, y

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

def rk4(f, x0, y0, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x0, y0

    for i in range(n):
        x[i + 1] = x[i] + h
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + (h / 2) * k1)
        k3 = f(x[i] + h / 2, y[i] + (h / 2) * k2)
        k4 = f(x[i] + h, y[i] + h * k3)

        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y 

def f(x, y):
    return x + y

def exact(x):
    return np.exp(x) - x - 1

def richardson(y_h, y_h2, p):
    return y_h2 + (y_h2 - y_h) / (2**p - 1)

x0, y0 = 0, 0
h = 0.1
n = 40

methods = {
    "Euler": (euler, 1),
    "Heun": (heun, 2),
    "RK4": (rk4, 4)
}

plt.figure(figsize=(10, 6))
x_exact = np.linspace(x0, x0 + n*h, n+1)
y_exact_vals = exact(x_exact)

for name, (method, p) in methods.items():
    x1, y1 = method(f, x0, y0, h, n)
    x2, y2 = method(f, x0, y0, h/2, 2*n)
    x4, y4 = method(f, x0, y0, h/4, 4*n)
    y_rich_h = richardson(y1, y2[::2], p)       
    y_rich_h2 = richardson(y2, y4[::2], p)       

    err_before = np.max(np.abs(y2[::2] - y_exact_vals))
    err_rich_h = np.max(np.abs(y_rich_h - y_exact_vals))
    err_rich_h2 = np.max(np.abs(y_rich_h2[::2] - y_exact_vals))
    rzad = np.log2(err_rich_h / err_rich_h2)

    print(f"{name} (wyjściowy rząd p={p}):")
    print(f"  Błąd przed Richardsonem: {err_before:.2e}")
    print(f"  Błąd po Richardsonie:      {err_rich_h:.2e}")
    print(f"  Nowy rząd metody:       ~{rzad:.2f}\n")
    plt.plot(x1, y_rich_h, label=f"{name} + Richardson")
      
plt.plot(x_exact, y_exact_vals, "k-", linewidth=2, label="Dokładne")
plt.title("Metody numeryczne i ekstrapolacja Richardsona")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

