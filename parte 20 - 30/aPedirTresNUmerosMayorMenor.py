
num1 = int(input('Primer numero ===> '))
num2 = int(input('Segundo numero ===> '))
num3 = int(input('Tercer numero ===> '))
if num1 >= num2 and num2 >= num3:
    print(f'El num1 es Mayor que: {num1} ')
elif num2 >= num1 and num1 >= num3:
    print(f'El num2 es Mayor que: {num2} ')
elif num3 >= num1 and num1 >= num2:
    print(f'El num3 es mayor que: {num3} ')
