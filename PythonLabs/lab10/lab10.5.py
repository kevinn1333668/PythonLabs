import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Данные
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Среднеквадратичная ошибка MSE - пример функции
Z = (X - 2)**2 + (Y - 3)**2

fig = plt.figure(figsize=(12, 6))

# Обычный масштаб
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE обычный масштаб')

# Логарифмический масштаб по z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zscale('log')
ax2.set_title('MSE логарифмический масштаб по z')

plt.tight_layout()
plt.show()