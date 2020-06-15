# Hacer un programa que pida un caracter  e indique si es una vocal o no
letra = input('Ingrese una letra: ').lower();
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Es una vocal')
else:
    print('No es una vocal')
