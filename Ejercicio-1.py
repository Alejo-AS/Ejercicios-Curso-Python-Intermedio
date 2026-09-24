#Práctica 1: Conjuntos

# Defino dos conjuntos A y B

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1)Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se 
# encuentran en A o en B, o en ambos.

union = A | B
print("1. Unión A | B:", union)

# 2)Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se 
# encuentran en A y en B

interseccion = A & B
print("2. Intersección A & B:", interseccion)

# 3)Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos 
# que se encuentran en A o en B, pero no en ambos.

diferencia_simetrica = A ^ B
print("3. Diferencia simétrica A ^ B:", diferencia_simetrica)

# 4)Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto 
# de otro conjunto, B.

es_subconjunto = A.issubset(B)
print("4. ¿A es subconjunto de B?", es_subconjunto)

# 5)Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.

cantidad = len(A)
print("5. Número de elementos de A:", cantidad)