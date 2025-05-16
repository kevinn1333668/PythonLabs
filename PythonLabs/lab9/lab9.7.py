import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species = iris[:, 4]

unique, counts = np.unique(species, return_counts=True)
print("Unique species:", unique)
print("Counts:", counts)