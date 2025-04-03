

# Задание 0
def task0(numbers):
    result = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            result.append(numbers[i])
    return result

# Задание 1
def task1(numbers):
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    min_index = numbers.index(min_val)
    max_index = numbers.index(max_val)

    new_numbers = numbers.copy()
    new_numbers[min_index], new_numbers[max_index] = new_numbers[max_index], new_numbers[min_index]

    return new_numbers

# Задание 2
def task2(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    return len(common)

# Задание 3
def task3(strings):
    count_dict = {}
    for s in strings:
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1

    result = list(count_dict.values())
    if len(result) == 1:
        return f"{result[0]}."
    else:
        return " ".join(map(str, result)) + "."