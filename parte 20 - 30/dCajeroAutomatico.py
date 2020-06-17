# Cajero Automatico
saldoInicial = 1000
print(' MENU:')
print('1._ : INGRESAR DINERO:')
print('2._ : RETIRAR DINERO:')
print('3._ : MOSTRAR DINERO:')
print('4._ : SALIR')

option = int(input('Ingrese la opciòn'))
if option == 1:
    aumentarDinero = int(input('Ingrese la cantidad de dinero'))
    result = saldoInicial + aumentarDinero
    print(f'Tu saldo actual es { result }')
elif option == 2:
    disminuirDinero = int(input('Ingrese la cantidad disminuir Dinero'))
    if disminuirDinero == saldoInicial:
        print('No puedes dejar tu cuenta vacia')
    elif disminuirDinero > saldoInicial:
        print('Tu retiro es mayor a la cantidad que contines en el banco')
    else:
        result = saldoInicial - disminuirDinero
        print(f'Tu saldo actual es { result }')
elif option == 3:
    print(f'Tu saldo total es: { saldoInicial }')
elif option == 4:
    print(f'Gracias por visitarnos vuelva pronto...')
