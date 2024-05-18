import numpy as np
matriz_a = np.array([[1,-5,9],[-8,-7,-6]])
matriz_b = np.array([[1],[6],[6]])
print(f'Matriz b normal : \n{matriz_b}')

# Transpuesta de una matriz
matriz_b_transpuesta = np.transpose(matriz_b)
print(f'Matriz b transpuesta: {matriz_b_transpuesta}')

# Resolución de una ecuación
# Ax = b (A y b son matrices)
matriz_a = np.array([[2,1,-2], [3,0,1], [1,1,-1]])
matriz_b = np.array([[-3],[5],[-2]])
matriz_b_transpuesta = np.transpose(matriz_b)

# Calculo de la matriz de los valores de x
matriz_x = np.linalg.solve(matriz_a, matriz_b)
print(matriz_x)

# Proceso para ver si los resultados de x son verdaderos
print(np.allclose(np.dot(matriz_a,matriz_x), matriz_b))

# Otro ejercicio de la forma:
'''
2x + 7y +3z = 1
2x + 8y + 2z = 1
x  + 3y + z = 0
'''
# Matriz de coeficientes
m_coeficientes = np.array([[2,7,3],[2,8,2],[1,3,1]])
# Matriz de términos independientes
m_ter_independientes = np.array([[1],[1],[0]])
m_ter_independientes_trans = np.transpose(m_ter_independientes)
#Soluciones
soluciones = np.linalg.solve(m_coeficientes,m_ter_independientes)
x, y , z = soluciones
print(f'''
Valor de x {x}
Valor de y {y}
Valor de z {z}
''')