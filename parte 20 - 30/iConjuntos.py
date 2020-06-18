# Conjuntos
# Conjuntos nos muestra cunado existe un numero repetitivo ya no se mostarar lo quitara
print('Conjuntos nos muestra cunado existe un numero repetitivo ya no se mostarar lo quitara')
conjunto = set()
conjunto = {1,2,3,4,5,1}
conjunto.add(4)
conjunto.add(6)
print(conjunto)

# Para quitar del conjunto
print('Para quitar del conjunto')
conjuntoA = set()
conjuntoA = {1,2,3}
conjuntoA.discard(1)
print(conjuntoA)


# Para limpiar un conjunto
print('Para limpiar un conjunto')
conjuntoB = set()
conjuntoB = {1,2,3}
conjuntoB.clear()
print(conjuntoB)

# Para Buscar en un conjunto
print('Para Buscar en un conjunto')
conjuntoB = set()
conjuntoB = {1,2,3}
conjuntoB1 = 1 in conjuntoB
print(conjuntoB1)

# Existe el item en un conjunto pero lo niega y lo manda false
print('Existe el item en un conjunto pero lo niega y lo manda false')
conjuntoB = set()
conjuntoB = {1,2,3}
conjuntoB1 = 1 not in conjuntoB
print(conjuntoB1)