# Comparar dos conjuntos y si ellos estan desordenados pero contine los mismos items dara true caso contraio false
print('Comparar dos conjuntos y si ellos estan desordenados pero contine los mismos items dara true caso contraio false')
conjunto = set()
conjuntoA1 = {1,2,3}
conjuntoA2 = {2,3,1}
result = conjuntoA1 == conjuntoA2
print(result)

# Ver tamaño
print('Ver tamaño')
conjuntoB = set()
conjuntoB1 = {1,2,3}
conjuntoB2 = {2,3,1}
print(len(conjuntoB1))

#unir dos conjuntos y quita los que estan repetidos
print('unir dos conjuntos  y quita los que estan repetidos')
conjuntoC = set()
conjuntoC1 = {1,2,3}
conjuntoC2 = {1,2,4}
result = conjuntoC1 |   conjuntoC2
print(result)


# Solo muestra los numeros repetidos en el conjunto
print('Solo muestra los numeros repetidos en el conjunto')
conjuntoD = set()
conjuntoD1 = {1,2,3}
conjuntoD2 = {3,1,5}
result = conjuntoD1 & conjuntoD2
print(result)


# MUestra los elementos en el conjunto a todos los que no se repiten
print('MUestra los elementos en el conjunto A...en  todos los que no se repiten')
print('entre el A y el B')
conjuntoE = set()
conjuntoE1 = {1,2,3}
conjuntoE2 = {3,1,5}
result = conjuntoE1 - conjuntoE2
print(result)


# MOstrar los conjuntos a y b
print('MOstrar los conjuntos a y b')
conjuntoF = set()
conjuntoF1 = {1,2,3}
conjuntoF2 = {3,1,5}
result = conjuntoF1 ^ conjuntoF2
print(result)


# Saber si un conjunto es subconjunto
print('Saber si un conjunto es subconjunto')
conjuntoG = set()
conjuntoG1 = {1,2}
conjuntoG2 = {4,5,6}
conjuntoG3 = {1,2,3,4,5,6}
print(conjuntoG1.issubset(conjuntoG3))

# Saber el superConjunto
print('Saber el superConjunto')
conjuntoH = set()
conjuntoH1 = {1,4}
conjuntoH2 = {1,2,3,4}
conjuntoH3 = {1,2,3,4}
print(conjuntoH3.issuperset(conjuntoH1))

#SAber si comparten algun conjunto en comun
print('SAber si comparten algun conjunto en comun')
conjuntoI = set()
conjuntoI1 = {5}
conjuntoI2 = {1,2,3,4}
print(conjuntoI1.isdisjoint(conjuntoI2))

#Conjuntos Inmutables
print('Conjuntos Inmutables')
print('NO SE PUEDE ADD REMOVE')
conjuntoJ = set()
conjuntoJ1 = frozenset({5})
print(conjuntoJ1)










