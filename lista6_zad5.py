from zad3 import *
import math
import numpy as np

def romberg_v2(f, a, b, d=15):
    n0=200
    R = [[0]*(n0+1) for _ in range(n0+1)]
    k=1
    while True:
        k+=1
        R[k][0] = trapez(f, a, b, 2**k)
        for j in range(1, k+1):
            R[k][j] = (4**j * R[k][j-1] - R[k-1][j-1]) / (4**j - 1)


        if k-3>=n0:
            n0*=2
            R.extend([[0] * (len(R[0]) + n0) for _ in range(n0)])
    
            for row in R[:-n0]:
                 row.extend([0] * n0)

        if abs(R[k][k] - R[k-1][k-1]) < 10**(-d):
            break

    return R[k][k]

print( romberg_v2(lambda x: np.exp(x), 0, 1, 2) - np.exp(1)+1)
print (np.exp(1)-1)
math.pi