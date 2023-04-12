# 4- Escribir un programa que solicite ingresar n notas de alumnos y nos informe cuántos
# tienen notas mayores o iguales a 7 y cuántos menores. Cuando ingresa nota=0 termina la
# ejecución

aprobados= 0
desaprobados = 0
nota = 1
while nota != 0:
    nota = int(input('ingrese nota:'))
    if nota >= 7:
        print('Nota igual o mayor a 7: ', nota)
        aprobados += 1
    else:
        print('Nota igual o menor a 7: ', nota)
        desaprobados += 1

print("Cantidad de alumnos con nota mayor o igual a 7:", aprobados)
print("Cantidad de alumnos con nota menor a 7:", desaprobados)