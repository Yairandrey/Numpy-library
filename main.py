import numpy as np
import array as ar

'''
Lista: 
*Es una colección de elementos pertenecientes a diferentes tipos de datos. 
*No se pueden manejar operaciones aritméticas directamente. 
*Usada para generar una secuencia corta.


Array: 
*Es una colección de elementos que pertenecen al mismo tipo de dato. 
*Sí se pueden manejar operaciones aritméticas directamente. 
*Usada para generar muchos elementos.
'''


# Trabajando arrays usando la librería {array}
# Colección con datos enteros (int)
matriz_enteros = ar.array('i',[1,2,3,4,5,6,7,8,9,10,0]) 
print(matriz_enteros)
for numero in matriz_enteros:
    print(numero)

# Colección con datos decimales (double)
matriz_decimales = ar.array('d',[1,6.9,0])
print(matriz_decimales)

# Trabajando arrays usando la librería {numpy}
matriz = np.array([2,4,6,7,7,5,5,0])
print(matriz)

lista = [1,3,5,7,9]
matriz = np.array([2,4,6])

# Le agrega a cada valor porque son elementos independientes.
matriz = matriz + np.array([8])

lista.append(7)
print(lista)
print(matriz)


a = [1,2,4,7]
b = [3,4,5,7]
print(a+b)

# Suma de dos matrices
c = np.array([1,2,4])
d = np.array([3,7.8,9])
print('SUMA: ',c+d)
print('MULT:', c*d)

