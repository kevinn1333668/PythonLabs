import numpy as np

a = np.arange(16).reshape(4,4)
print("Изначальный массив:\n", a)

a[[1,3]] = a[[3,1]]

print("После замены строк:\n", a)