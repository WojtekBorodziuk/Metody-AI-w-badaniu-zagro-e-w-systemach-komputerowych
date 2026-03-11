import numpy as np 
import matplotlib.pyplot as plt

tabela = np.ones((3, 5, 7))

tabela = tabela.astype(int)

suma1 = np.sum(tabela, axis=0)
print(suma1)
print("shape:", suma1.shape)


suma2 = np.sum(tabela, axis=1)
print(suma2)
print("shape:", suma2.shape)


suma3 = np.sum(tabela, axis=2)
print(suma3)
print("shape:", suma3.shape)


