# Escriba un programa donde tenga una lista y que, 
# a continuación, elimine los elementos repetidos, 
# por último mostrar la lista

# Colas
print('Colas')
cola = ['vanessa',1,2,'erika',1,5,'erika']
conjunto = set(cola)
onLista = list(conjunto)
print(onLista)

# Colas acortando codigo
print('Colas acortando codigo')
cola = ['vanessa',1,2,'erika',1,5,'erika']
onLista = list(set(cola))
print(onLista)