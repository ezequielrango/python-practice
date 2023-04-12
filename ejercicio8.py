# 8- Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y
# luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté
# comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de
# piezas aptas que hay en el lote.

cantidadPiezas= int(input('Ingresar n piezas:'))
i = 0
piezasAptas= 0
while i < cantidadPiezas:
        longitudPerfil = float(input('Ingresar longitud perfil:'))
        if longitudPerfil >= 1.20 and longitudPerfil <= 1.30:
            piezasAptas += 1
        i += 1
        
print('Piezas aptas: ', piezasAptas)
