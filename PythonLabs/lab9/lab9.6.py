import numpy as np

a = np.arange(16).reshape(4,4)
print("Original array:\n", a)

a[[1, 3]] = a[[3, 1]]
print("Array after swapping rows 1 and 3:\n", a)