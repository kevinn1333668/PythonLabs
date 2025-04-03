# Задание 1
def task1(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


# Задание 2
def task2(set1, set2):
    if set1 == set2:
        return False
    return set1.issubset(set2)


# Задание 3
def task3():
    n = int(input("Введите количество названных городов: "))
    cities = set()

    for _ in range(n):
        city = input().strip()
        cities.add(city)

    new_city = input("Введите новый город: ").strip()

    if new_city in cities:
        print("REPEAT")
    else:
        print("OK")