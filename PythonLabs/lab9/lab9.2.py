import numpy as np

def run_length_encoding(x):
    n = len(x)
    if n == 0:
        return np.array([]), np.array([])

    # Находим индексы, где значения меняются
    diff = np.diff(x)
    change_indices = np.where(diff != 0)[0] + 1

    # Добавляем начальный и конечный индексы
    indices = np.concatenate(([0], change_indices, [n]))

    values = x[indices[:-1]]
    counts = np.diff(indices)

    return values, counts

x = np.array([2, 2, 2, 3, 3, 3, 5])
print(run_length_encoding(x))