import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Временная ось (например, 2 периода сигнала)
t = np.linspace(0, 2, 1000, endpoint=False)

# Генерация прямоугольного сигнала с частотой 5 Гц
frequency = 5  # в герцах
signal = square(2 * np.pi * frequency * t)

# Отрисовка сигнала
plt.figure(figsize=(9,4))
plt.plot(t, signal)
plt.title('Прямоугольный сигнал (Square Wave)')
plt.ylabel('Амплитуда')
plt.xlabel('Время, сек')
plt.grid(True)
plt.ylim([-1.5, 1.5])
plt.show()