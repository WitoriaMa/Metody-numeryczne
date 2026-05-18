import numpy as np
from z1 import *
from z2 import *
n=50
#A =np.random.rand(n,n)
#A[-1,:] = A[-2,:] + 10**(-16)
#b = b = A @ x + 10**(-8) * np.random.randn(n)
#x4 = np.linalg.solve(A, b)
#A_np = np.array(A, dtype=float)
#b_np = np.array(b, dtype=float)
#def hilbert(n):
#   return np.array([[1/(i+j+1) for j in range(n)] for i in range(n)])
n=5

A = np.random.rand(n, n)
x_true = np.ones(n)
b = A @ x_true
print(b)
n=len(A)
x=np.linalg.solve(A, b)

def norma(A, x, b):
    r = A @ x - b
    print(r)
    return np.linalg.norm(r)

print("Gauss-Jordan")
x1 = gauss(A.copy(), b.copy())
print("x =", x1)
print("norma reszt =", "{:.20e}".format(norma(A, x1, b)))
print()

print("Solve")
x2 = np.linalg.solve(A, b )
print("x =", x2)
print("{:.20e}".format(norma(A, x2, b)))        
print()

print("Jacobi")

for it in [n, n**2, n**3]:
    x3 = jakobi(A.copy(), b.copy(), it)
    err = norma(A.copy(), x3, b.copy())

    print("iteracje =", it)
    print("x =", x3)
    print("norma reszt =", "{:.20e}".format(err))
    print()
