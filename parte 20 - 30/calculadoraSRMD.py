num1 = float(input('Ingrese el primer numero'))
num2 = float(input('Ingrese el segundo numero'))
operacion = input('Ingrese la operacion').upper();
if operacion == 'S':
    result = num1 + num2
    print(f'La suma es: { result }')
elif operacion == 'R':
    result = num1 - num2
    print(f'La restar es: { result }')
elif operacion == 'M':
    result = num1 * num2
    print(f'La Multiplicaion es: { result }')
elif operacion == 'D':
    result = num1 / num2
    print(f'La Divicion es: { result }')
else:
    print('Ups.. te equivocaste de operacion')

