import numpy as np
import matplotlib.pyplot as plt


np.random.seed(1)
a1 = np.random.normal(loc=0, scale=1, size=(30, 2))
a2 = np.random.normal(loc=[1, 3], scale=3, size=(130, 2))


fig, ax = plt.subplots(1, 1, figsize=(5, 5))

ax.scatter(a1[:, 0], a1[:, 1], color='red', marker='x', label='a1')


ax.scatter(a2[:, 0], a2[:, 1], color='blue', label='a2')


ax.legend()

ax.grid()

plt.tight_layout()

plt.savefig("zadanie3.png")

plt.show()



