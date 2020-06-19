# Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

#- Lista de elementos que aparecen en las dos listas.
#- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
#- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
#- Lista de elementos que aparecen en ambas listas.

list1 = [1,2,5,4,5,2,3,6,7,8]
list2 = [2,4,5,2,3,6,4,5,2,4]

# Eliminamos los valores iguales en cada lista
a = set(list1)
b = set(list2)

union = list( a | b )
soloA = list( a - b )
soloB = list( b - a )
interseccion = list( a & b )

print(f'Lista de elementos que aparecen en la dos listas { union }')
print(f'Lista de elemntos que aparecen en la primera lista, pero no en la segunda lista { soloA }')
print(f'Lista de elemntos que aparecen en la segunda lista, pero no en la primera lista { soloB }')
print(f'Lista de elementos que aparecen en ambas listas { interseccion }')