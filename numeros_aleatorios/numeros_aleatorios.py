import numpy as np

# Números aleatorios enteros con límite y una cantidad de elementos
matriz_aleatoria = np.random.randint(10, size=(5))
print(matriz_aleatoria)


matriz_a = np.random.randint(20, size = (4,3))
print(matriz_a)
# Números aleatorios decimales
matriz_b = np.random.rand(2,2)
print(matriz_b)

# Escoger un número dentro de la matriz
matriz_c = np.random.choice([3,56,4,3,4,5,666] ,size=(2,3))
print(matriz_c)

# Distribución aleatoria basadose en una matriz de probabilidades por cada número
matriz = np.random.choice\
    ([2,4,8,10], p = [0.25,0.25,0.25,0.25], size =[50,2])
print(matriz)