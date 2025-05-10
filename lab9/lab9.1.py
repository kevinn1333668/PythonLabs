import numpy as np


# Читаем матрицу из файла
matrix = np.loadtxt('lab9/matrix.txt', delimiter=',')

# Выводим сумму, мин и макс
print("Сумма элементов:", matrix.sum())
print("Максимальный элемент:", matrix.max())
print("Минимальный элемент:", matrix.min())