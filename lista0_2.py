import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 0, 500)


L=[1]
for i in range(1, 11):
    L.append(L[-1]*x/i)
S10=sum(L)

y = np.exp(x)


plt.figure(figsize=(10,5))
plt.plot(x, y, label='e^x', color='violet')
plt.plot(x, S10, label='10 wyrazów Maclaurina', color='blue', linestyle='--')
plt.title(' e^x vs. S10')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-1,5)
plt.grid(True)
plt.show()

#od pewnego mometu jest idealne przybliżenie