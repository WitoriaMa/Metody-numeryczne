import numpy as np
import matplotlib.pyplot as plt
sigma = 10
r = 28
b = 2

def lorky(x, y, z):
    dx = sigma * (y - x)
    dy = -x*z + r*x - y
    dz = x*y - b*z
    return dx, dy, dz


def rk4_lorky(x0, y0, z0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    z = np.zeros(n+1)
    t = np.zeros(n+1)

    x[0], y[0], z[0] = x0, y0, z0

    for i in range(n):
        k1x, k1y, k1z = lorky(x[i], y[i], z[i])
        k2x, k2y, k2z = lorky(
            x[i] + h*k1x/2,
            y[i] + h*k1y/2,
            z[i] + h*k1z/2
        )

        k3x, k3y, k3z = lorky(
            x[i] + h*k2x/2,
            y[i] + h*k2y/2,
            z[i] + h*k2z/2
        )

        k4x, k4y, k4z = lorky(
            x[i] + h*k3x,
            y[i] + h*k3y,
            z[i] + h*k3z
        )

        x[i+1] = x[i] + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        y[i+1] = y[i] + (h/6)*(k1y + 2*k2y + 2*k3y + k4y)
        z[i+1] = z[i] + (h/6)*(k1z + 2*k2z + 2*k3z + k4z)

        t[i+1] = t[i] + h

    return t, x, y, z



x0, y0, z0 = 2,3,4
h = 0.01
n = 10000

t, x, y, z = rk4_lorky (x0, y0, z0, h, n)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, linewidth=0.5)

ax.set_title("Wykres 3D)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()

plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("z")
plt.title("Atraktor Lorenza")
plt.show()