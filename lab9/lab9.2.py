import numpy as np

def run_length_encoding(x):
    nums = [x[0]]
    counts = [1]
    print(x[0])

    for el in x[1:]:
        if el == nums[-1]:
            counts[-1] += 1
        else:
            nums.append(el)
            counts.append(1)
    return np.array(nums), np.array(counts)

x = np.array([2, 2, 2, 3, 3, 3, 5])
num, cnt = run_length_encoding(x)
print("Элементы:", num)
print("Количество повторений:", cnt)