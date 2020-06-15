num1 = int(input('Primer numero'))
num2 = int(input('Segundo numero'))
if num1%2 == 0 and num2%2 != 0:
    print('Es un num1 par')
elif num1%2 != 0 and num2%2 == 0:
    print('Es un num2 impar')
elif num1%2 == 0 and num2%2 == 0:
    print('Amos son impares')
else:
    print('Son Impares')
