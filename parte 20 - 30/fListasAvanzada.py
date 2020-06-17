listA = ['a','b','c','d']
print(len(listA))
print(listA)
# agregar un objeto mas
print('aumentamos uno mas')
listB = ['a','b','c','d']
listB.append('e')
print(listB);
#agregamos un item como string
print('agregamos uno que tiene string')
listaC = ['a','b']
listaC.append('c')
listaC.append('faby')
print(listaC)
#agregamos el item de acuerdo a la pocision con insert
print('Agregamos un item de acuerdo a a pociion que uno decea')
listD = ['ambar','lynna']
listD.insert(1,'erika')
print(listD)
#Extender un arreglo
print('Extendemos el arreglo')
listE = [1,2,3,4]
listE.extend([5,6,7,8])
print(listE)

#combinar dos arreglos
print('Conmibar dos arreglos')
listF = [1,2]
listF1 = [3,4]
listF2 = listF + listF1
print(listF2)

#Saber si existe ese elemento en el arreglo
print('Saber si ecsiste un elemto en un arreglo')
listG = [1,2,3]
listG1 = 1  in listG
print(listG1)

# saber en que pocicion se encuentra el elemnto
print('saber en que pocicion se encuentra el elemnto')
listH = [1,2,3]
print(listH.index(1))

# para saber cuantos exosten en el mismo arreglo
print('para saber cuantos exosten en el mismo arreglo')
listI = [1,2,3,1]
print(listI.count(2))

# Para eliminar el ultimo item
print('Para eliminar el ultimo item')
listI = [1,2,3,1,'star']
listI.pop()
print(listI)

# Para eliminar segun la pocicion
print('Para eliminar segun la pocicion')
listJ = [1,2,3,1,'star']
listJ.pop(1)
print(listJ)


# Para remover segun el nombre
print('Para remover segun el nombre')
listJ = [1,2,3,1,'star']
listJ.remove('star')
print(listJ)


# Para limiar 
print('Para limpiar')
listK = [1,2,3,1,'star']
listK.clear()
print(listK)

# Para invertir
print('Para limpiar')
listL = [1,2,3,1,'star']
listL.reverse()
print(listL)

# Para Duplicar el arreglo
print('Para Duplicar el arreglo')
listL = [1,2,3,1,'star']*2
print(listL)

# para sortear en el orden correspondiente
print('para sortear en el orden correspondiente')
listM = [1,2,3,4,-5]
listM.sort()
print(listM)

# para sortear de forma invertida en el orden correspondiente
print('para sortear de forma invertida en el orden correspondiente')
listN = [1,2,3,4,-5]
listN.sort(reverse=True)
print(listN)

