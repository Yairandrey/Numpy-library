import numpy as np
matriz = np.arange(24).reshape(4,6)
print(f'Matriz: \n {matriz}')
# Llamar un valor por indices
print(matriz [3,4])

matriz_a = np.array([6,3,5,8])
# Odenando el array (1D)
print(f'Matriz a ordenada de menor a mayor: {np.sort(matriz_a)}')

matriz_de_bool = np.array(matriz_a >= 2)
print(matriz_de_bool)

# Valor máximo de la matriz
maximo = np.array(matriz_a.max())
print(f'Numero máximo de matriz a  es: {maximo}')

matriz_b = np.array([3,2,9,6])

# Potencia de la matriz
potencia = (np.power(matriz_b,3))
print(f'Potencia es: {potencia}')

# Combinar 2 matrices
combinacion = np.concatenate((matriz_a, matriz_b))
print(f'concatenación de matrices: {combinacion}')

# Suma de matrices
suma = matriz_a + matriz_b
print(f'suma de matriz a y matriz b es: {suma}')

matriz_c = np.array([[4,5,2],[4,0,0]])
matriz_d = np.array([[34,67,45],[12,45,34]])

suma = matriz_c + matriz_d
print(f'Suma de c y d: \n{suma}')

print(matriz_c + 2)

print(np.add(matriz_c, matriz_d))
print(np.subtract(matriz_a, matriz_b))
print(np.multiply(matriz_a, matriz_b))
print(np.divide(matriz_a, matriz_b))


print(f'Matriz con .dot: {matriz_a.dot(matriz_b)}')