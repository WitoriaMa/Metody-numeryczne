import numpy as np
def jakobi(A, b, iterations):
    n = len(A)
    x = [0.0] * n
    for _ in range(iterations):
        x2 = [0.0] * n

        for i in range(n):
            s = 0.0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x2[i] = (b[i] - s) / A[i][i]
        x = x2
    return x

A=np.array([[1,0.1], [0.1,1]])
b=np.array([1,1])
print(jakobi(A, b, 100))