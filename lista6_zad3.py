from zad1 import *

def romberg(f, a, b, k=4,):
    R = [[0]*(k+1) for _ in range(k+1)]

    for i in range(k+1):
        R[i][0] = trapez(f, a, b, 2**i)

        for j in range(1, i+1):
            R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)

    return R[k][k]

def main():
    print(romberg(lambda x: x**2, 0, 1, 4)-1/3)
    print(romberg(lambda x: x**3, 0, 1, 4)-1/4)
    print(romberg(lambda x: x**4, 0, 1, 4)-1/5)
    print(romberg(lambda x: x**5, 0, 1, 4)-1/6)
    print(romberg(lambda x: x**6, 0, 1, 4)-1/7)
    print(romberg(lambda x: x**7, 0, 1, 4)-1/8)
    print(romberg(lambda x: x**8, 0, 1, 4)-1/9)

if __name__ == "__main__":
    main()


