print('Mostrando diaz de nacimiento')
coleccion = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(coleccion[29])
print('================')
print('Mostrando si existe la persona o no')
print(coleccion.get(8,'No existe esa persona con su dia de nacimiento'))
print('==============')
print('Mostrar true si existe y false si no existe')
coleccionA = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(8 in coleccionA)
print('=============')
print('Mostarr por clave')
coleccionB = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(coleccionB.keys())

print('=============')
print('Mostarr por valor')
coleccionC = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(coleccionC.values())


print('=============')
print('Mostarr por items')
coleccionC = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(coleccionC.items())

print('=============')
print('Mostarr por el tamaño')
coleccionC = {23:  'ambar', 8: 'lynna', 29: 'erika'}
print(len(coleccionC))

print('=============')
print('limpiar')
coleccionD = {23:  'ambar', 8: 'lynna', 29: 'erika'}
coleccionD.clear()
print(coleccionD)
