
from scipy.integrate import quad
import math

L=[math.log(6/5)]
N = 24
for n in range(1, N+1):
    L.append(1/n - 5*L[n-1])

for n in range(N+1):
    f= lambda x: x**n/(x+5)
    dokladna = quad(f, 0, 1)
    rekurencja = L[n]
    roznica= rekurencja-dokladna[0]
    print(f"n = {n}")
    print("rekurencja =", rekurencja)
    print("dokładna =", dokladna)
    print("różnica =", abs(roznica))

#im większe n tym gorsze przybliżenie, ponieważ jest to rekurencja (lemat Wilkinsona-wykład)
