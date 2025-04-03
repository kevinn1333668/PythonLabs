# Задание 1
def task1():
    with open('input.txt', 'w') as f:
        f.write("2 3 5 7 11 13 17 19 23 29")

    with open('input.txt', 'r') as f:
        numbers = list(map(int, f.read().split()))

    product = 1
    for num in numbers:
        product *= num

    with open('output.txt', 'w') as f:
        f.write(str(product))


# Задание 2
def task2():
    with open('input2.txt', 'w') as f:
        f.write("17\n23\n5\n11\n29\n2\n13\n7\n3\n19\n")

    with open('input2.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f]

    numbers.sort()

    with open('output2.txt', 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")


# Задание 3
def task3():

    with open('children.txt', 'w', encoding='utf-8') as f:
        f.write("Иванов Иван 5\n")
        f.write("Петров Петр 6\n")
        f.write("Сидоров Алексей 4\n")
        f.write("Кузнецова Мария 7\n")
        f.write("Смирнова Анна 3\n")

    children = []
    with open('children.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            surname, name, age = parts[0], parts[1], int(parts[2])
            children.append((surname, name, age))


    oldest = max(children, key=lambda x: x[2])
    youngest = min(children, key=lambda x: x[2])


    with open('oldest.txt', 'w', encoding='utf-8') as f:
        f.write(f"{oldest[0]} {oldest[1]} {oldest[2]}")

    with open('youngest.txt', 'w', encoding='utf-8') as f:
        f.write(f"{youngest[0]} {youngest[1]} {youngest[2]}")
