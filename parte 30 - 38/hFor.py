#  BUcle for

# Mostrando datos de la colecion
coleccion = {'1':'vanessa','2':'ambar','3':'erika','4':'lynna'}
for i in coleccion:
    print(f'{ i } ===> { coleccion[i] }')


# Otra forma
# Mostrando datos de la colecion
print('=======')
print('Otra forma')
print('Mostrando datos de la colecion')
coleccion = {'1':'vanessa','2':'ambar','3':'erika','4':'lynna'}
for clave, valor in coleccion.items():
    print(f'{ clave } ===> { valor }')


# Deletrear vocal por vocal vertical
print('=======')
print('Deletrear vocal por vocal vertical')
palabra = 'Erika'
for i in palabra:
    print(i)


# Deletrear vocal por vocal Horizontal
print('=======')
print('Deletrear vocal por vocal horizontal')
palabra = 'ambar'
for i in palabra:
    print(f'{i}',end = "♥")


# Deletrear vocal por vocal Horizontal
print('=======')
print('Deletrear vocal por vocal horizontal')
palabra = 'lynna'
for i in palabra:
    print(f'{i}',end = "♥")

# Deletrear vocal por vocal Horizontal
print('=======')
print('Deletrear vocal por vocal horizontal')
palabra = 'mary'
for i in palabra:
    print(f'{i}',end = "♥")


# Deletrear vocal por vocal Horizontal
print('=======')
print('Deletrear vocal por vocal horizontal')
palabra = 'vanessa'
for i in palabra:
    print(f'{i}',end = "♥")