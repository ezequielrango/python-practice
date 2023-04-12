# 2- Desarrollar un programa que nos permita ingresar 10 número y nos diga si cada número
# es par o impar. Para lo cual utilizar el operador % que nos devuelve el resto de la División.

contador = 1
while contador <= 10:
    valor = int(input("Ingrese el valor " + str(contador) + ": "))

    if valor % 2 == 0:
        print("El siguiente valor es par: ", valor)
    else: 
        print("El siguiente valor es impar: ", valor)
        contador += 1
