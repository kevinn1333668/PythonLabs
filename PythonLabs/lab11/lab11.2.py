import numpy as np
import matplotlib.pyplot as plt

# Генерируем нормальное распределение
data = np.random.randn(10000)

# Гистограмма данных
plt.figure(figsize=(8,4))
plt.hist(data, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black')

plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.grid(True)
plt.show()