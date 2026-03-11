import numpy as np

np.random.seed(1)

a1 = np.random.normal(loc=0, scale=1, size=(30, 2))

a2 = np.random.normal(loc=[1, 3], scale=3, size=(130, 2))

print(a1[:, 0])

print(a2[-1])