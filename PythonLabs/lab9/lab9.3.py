import numpy as np

np.random.seed(42)  # Для воспроизводимости
arr = np.random.randn(10, 4)  # нормальное распределение

min_val = np.min(arr)
max_val = np.max(arr)
mean_val = np.mean(arr)
std_val = np.std(arr)

first_five_rows = arr[:5]

print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val}, Std: {std_val}")
print("First 5 rows:\n", first_five_rows)