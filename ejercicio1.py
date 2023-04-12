# 1-Desarrollar un programa que permita la carga de 12 valores por teclado y nos muestre
# posteriormente la suma de los valores ingresados y su promedio. El resultado del promedio
# es un valor real es decir con coma. Si queremos que el resultado de la división solo retorne
# la parte entera del promedio debemos utilizar el operador //: promedio=suma//12
suma = 0
contador = 1

while contador <= 12:
    valor = int(input("Ingrese el valor " + str(contador) + ": "))
    suma += valor
    contador += 1

promedio = suma / 12

promedio = suma // 12

print("La suma de los valores ingresados es:", suma)
print("El promedio de los valores ingresados es:", promedio)