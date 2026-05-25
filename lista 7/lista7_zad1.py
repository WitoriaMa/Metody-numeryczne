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

def main():
    x0, y0 = 0, 1
    h = 0.5
    n = 20

    def f_euler_p1(x, y):
        return 1
    def exact_euler_p1(x):
        return x + 1
    x_num, y_num = euler(f_euler_p1, x0, y0, h, n)
    err_euler_p1 = np.max(np.abs(y_num - exact_euler_p1(x_num)))
    print(f"Euler, st1, błąd: {err_euler_p1:.2e}")

    def f_euler_p2(x, y):
        return 2*x
    def exact_euler_p2(x):
        return x**2 + 1
    x_num, y_num = euler(f_euler_p2, x0, y0, h, n)
    err_euler_p2 = np.max(np.abs(y_num - exact_euler_p2(x_num)))
    print(f"Euler, st2, błąd: {err_euler_p2:.2e}")

    def f_heun_p2(x, y):
        return 2*x
    def exact_heun_p2(x):
     return x**2 + 1
    x_num, y_num = heun(f_heun_p2, x0, y0, h, n)
    err_heun_p2 = np.max(np.abs(y_num - exact_heun_p2(x_num)))
    print(f"Heun, st2, błąd: {err_heun_p2:.2e}")

    def f_heun_p3(x, y):
        return 3*x**2
    def exact_heun_p3(x):
         return x**3 + 1
    x_num, y_num = heun(f_heun_p3, x0, y0, h, n)
    err_heun_p3 = np.max(np.abs(y_num - exact_heun_p3(x_num)))
    print(f"Heun, st3, błąd: {err_heun_p3:.2e}")

    def f_rk4_p4(x, y):
        return 4*x**3
    def exact_rk4_p4(x):
        return x**4 + 1
    x_num, y_num = rk4(f_rk4_p4, x0, y0, h, n)
    err_rk4_p4 = np.max(np.abs(y_num - exact_rk4_p4(x_num)))
    print(f"RK4, st4, błąd: {err_rk4_p4:.2e}")

    def f_rk4_p5(x, y): 
        return 5*x**4
    def exact_rk4_p5(x):
        return x**5 + 1
    x_num, y_num = rk4(f_rk4_p5, x0, y0, h, n)
    err_rk4_p5 = np.max(np.abs(y_num - exact_rk4_p5(x_num)))
    print(f"RK4, st5, błąd: {err_rk4_p5:.2e}")

    def f1(x, y):
        return y
    x_e, y_e = euler(f1, x0, y0, h, n)
    x_h, y_h = heun(f1, x0, y0, h, n)
    x_r, y_r = rk4(f1, x0, y0, h, n)
    y_exact = np.exp(x_e)


    plt.figure(figsize=(8, 5))
    plt.plot(x_e, y_exact, 'k-', linewidth=2, label="Dokładne (exp(x))")
    plt.plot(x_e, y_e, "r--", label="Euler")
    plt.plot(x_h, y_h, "b-.", label="Heun")
    plt.plot(x_r, y_r, "g:", linewidth=2, label="RK4")
    
    plt.title("Porównanie metod dla równania y' = y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
