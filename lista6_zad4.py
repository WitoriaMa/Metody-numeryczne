import math
from zad3 import *


print("Bład 1: "+ str(romberg(lambda x: math.exp(x), 0, 1, 10) - math.exp(1)+1))
print("Błąd 2:" +str(romberg(lambda x: math.sin(x), 0, math.pi/2, 10) - 1)) 


