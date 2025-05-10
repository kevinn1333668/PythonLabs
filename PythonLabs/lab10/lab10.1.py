import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 400)
plt.figure(figsize=(10,6))

for n in range(1, 8):
    y = legendre(n)(x)
    #plt.plot(x, y, label=f'n = {n}')

# Реализация выносок (с помощью аннотаций)
for n, xpos in enumerate(np.linspace(-0.9, 0.9, 7), start=1):
    ymax = legendre(n)(xpos)
    plt.annotate(f'n = {n}', xy=(xpos, ymax), xytext=(xpos+0.1, ymax + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)

plt.title('Полиномы Лежандра')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()