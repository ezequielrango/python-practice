# 5- Ingresan las alturas n personas y se calcula el promedio. Preguntar cuántos datos se
# ingresarán

totalDatos= int(input('ingrese total de personas:'))
sumaAltura = 0
i= 0


while i < totalDatos:
    altura = int(input('ingrese su altura en cm:'))
    sumaAltura += altura
    i += 1

promedio = sumaAltura // totalDatos

print('Promedio de altura: ', promedio)
