import numpy as np
# Задача: найти максимальное значение в массиве, которое следует за нулем

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_indices = np.where(x[:-1] == 0)[0]
candidates = x[zero_indices + 1]
result = np.max(candidates)

print(result)  # Ответ: 5