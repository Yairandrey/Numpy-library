import numpy as np

matriz = np.array([[1,2,3], [3,5,6], [3,200,4]])
print(matriz)
print('')
# Calculo el maximo valor de la matriz
maximo = np.max(matriz)
print(maximo)

# Valor máximo usando a que se refiere a axis
maximo = np.amax(matriz)
print(maximo)

# Valor mínimo usando a que se refiere a axis
minimo = np.amin(matriz,0)
print(minimo)

# Calculo del rango
rango = np.ptp(matriz, axis=0)
print(f'Rango: {rango}')

#Percentiles

percentil_dos = np.percentile(matriz,50, axis = 1)
print(f'Percentil dos es {percentil_dos}')

percentil_tres = np.percentile(matriz,75, axis = 0)
print(f'Percentil tres es {percentil_tres}')


# Mediana
mediana_filas = np.median(matriz, axis=1)
print(f'Mediana por filas: {mediana_filas}')

mediana_columnas = np.median(matriz, axis=0)
print(f'Mediana por columnas: {mediana_columnas}')

# Media aritmética
media_aritmetica = np.mean(matriz)
print(f'Media aritmética es: {round(media_aritmetica,4)}')
print('Ahora se va a hacer uso de una matriz dimensional')
matriz_a = np.array([2,5,4,3,2])

# Promedio ponderado
promedio_ponderado = np.average(matriz_a)
print(f'Promedio ponderado es: {promedio_ponderado}')

# Desviación estándar
desviacion_estandar = np.std(matriz_a,)
print(f'Desviación estándar es {round(desviacion_estandar,4)}')