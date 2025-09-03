# Unión de conjuntos

conjunto_1 = {"sergio", "ana", "maria", "joaquin"}
conjunto_2 = {"ana", "maria", "laura", "carlos", "sergio", "javier"}

print (conjunto_1 | conjunto_2)


# Intersección de conjuntos

A = {"sergio", "ana", "maria", "joaquin"}
B = {"ana", "maria", "laura", "carlos", "sergio", "javier"}

print (A & B)

# Diferencia de conjuntos

C = {"sergio", "ana", "maria", "joaquin"}
D = {"ana", "maria", "laura", "carlos", "sergio", "javier"}

print (C - D)
print (D - C)

# subconjuntos
numero_1 = {1, 2, 3, 8, 6, 1, 4, 5}
numero_2 = {4, 5, 6, 4, 5, 7, 8}
numero_3 = {1, 2, 3}

print (numero_1.issubset(numero_2))
print (numero_2.issubset(numero_1))
print(numero_3.issubset(numero_1))

#cantidad de elementos en un conjunto
conjunto_a = {"a", 2, 9, 8, 4, 5, 6}
print(len(conjunto_a)) 

conunto_b = {"ana", "maria", "laura", "carlos", "sergio", "javier"}
print(len(conunto_b))