edad = int(input('INgresa la edad'));
if edad > 0 and edad < 18:
    print('Es menor de edad')
    if edad == 13:
        print('estas aun en la escuela')
elif edad >= 18:
    print('Es Mayor de edad')    
else:
    print('Edad erronea')