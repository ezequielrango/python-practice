# 7- Se necesita realizar un control de edad de ingreso al Sistema de una empresa. Mientras
# la edad sea entre 18 y 65 pueden acceder al sistema caso contrario mostrar Mensaje de
# Acceso Denegado

edad= int(input('Ingresar edad:'))


while True:
        if edad >= 18 and edad <=65:
            print('Puedes ingresar')
            break
        else:
            print('Acceso Denegado')
            break
