import numpy as np

# Генерация массива 10x4 нормального распределения
arr = np.random.randn(10,4)

# Нахождение значений
print("Минимум: ", arr.min())
print("Максимум: ", arr.max())
print("Среднее значение: ", arr.mean())
print("Стандартное отклонение: ", arr.std())

# Сохраняем первые 5 строк в отдельную переменную
first_five = arr[:5,:]
print("\nПервые 5 строк:\n", first_five)