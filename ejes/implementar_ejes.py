import numpy as np

matriz = np.array([[0,1,2,3], [5,7,9,6]])
matriz_a = np.array([[0,1,2,3], [5,4,9,61]])
print(matriz)
print('')
# El cero suma las columnas
# El uno suma las filas
print(np.sum(matriz, axis=0))

# Concatenar dos matrices dimensionales.
print(np.concatenate([matriz,matriz_a], axis=1))