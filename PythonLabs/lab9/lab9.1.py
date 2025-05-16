with open("lab9/matrix.txt", "r") as f:
    matrix = [list(map(int, line.strip().split(','))) for line in f]

# Шаг 3: Вычисляем сумму, максимум и минимум
total_sum = sum(sum(row) for row in matrix)
max_element = max(max(row) for row in matrix)
min_element = min(min(row) for row in matrix)

# Шаг 4: Выводим результаты
print("Сумма всех элементов:", total_sum)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)