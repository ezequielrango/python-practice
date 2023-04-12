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