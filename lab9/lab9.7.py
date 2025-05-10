import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# берем столбец species (последний)
species = iris[:, 4]

# уникальные значения и их кол-ва
unique_species, counts = np.unique(species, return_counts=True)

print("Уникальные виды:", unique_species)
print("Количество:", counts)