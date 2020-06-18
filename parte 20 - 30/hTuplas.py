tupla = (1,2,3,'faby star',[1,2,3],'joder')
print(tupla[2]) # de isquierda a derecha
print(tupla[-2]) # de derecha a isquierda
# Buscar dentro de una tupla
print('Buscar dentro de una tupla')
tuplaA = (1,2,3,4)
existe = 4 in tuplaA
print(existe)


# Mostrar en que pocicion se encuentra
print('Mostrar en que pocicion se encuentra')
tuplaB = (1,2,3)
print(tuplaB.index(2))

# Contar cuantos existen en la tupla
print('Contar cuantos existen en la tupla')
tuplaC = (1,2,3)
print(tuplaB.count(4))


# Mostrar el tamaño que tiene la tupla
print('Mostrar el tamaño que tiene la tupla')
tuplaD = (1,2,3)
print(len(tuplaB))

# MOstrar como un arreglo
print('Mostrar como arreglo')
tuplaE = (1,2,3,4)
listE = list(tuplaE)
print(listE)

# De arreglo a tupla
print('De arreglo a tupla')
arreglo = [1,2,3,4]
tuplaF = tuple(arreglo)
print(tuplaF)



