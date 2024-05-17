import numpy as np
matriz = np.arange(30).reshape(6,5)
# Función .shape me devuelve la cantidad de filas y columnas (tupla)
filas_columnas = matriz.shape
filas, columnas = matriz.shape
print(f'Tupla de data: {filas_columnas}')
print(f'Rows: {filas}')
print(f'Columnas: {columnas}')
print(matriz)

# Calcular número de dimensiones con .ndim
dimensiones = matriz.ndim
print(f'Dimensiones: {dimensiones}')

# Hallar el número total de elementos
total_elementos = matriz.size
print(f'Total elementos: {total_elementos}')

# Matriz llena de ceros
matriz_cero = np.zeros((3,5))
print(matriz_cero)

# Generar matriz definiendo primer(99) y último elemento(88) con un número de números a crear
matriz_n = np.linspace(99,88,30)
print(matriz_n)

# Matriz en 3D
matriz_3_d = np.arange(24).reshape(2,3,4)
print(f'Matriz en 3D: \n{matriz_3_d}')