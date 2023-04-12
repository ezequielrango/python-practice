# 6- En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
# cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
# informar el importe que gasta la empresa en sueldos al personal.


totalEmpleados= int(input('ingrese total de personas:'))
sueldosBajos= 0
sueldosAltos= 0
totalSueldos= 0
i= 0


while i < totalEmpleados:
    sueldo = int(input('ingrese su sueldo:'))
    totalSueldos += sueldo
    i += 1
    if sueldo >= 100 and sueldo <= 300:
        sueldosBajos += 1
    elif sueldo > 300:
        sueldosAltos += 1

print('Total gastos sueldos', totalSueldos)
print("La cantidad de empleados que ganan entre $100 y $300 es:",sueldosBajos)
print("La cantidad de empleados que ganan entre $300 y $500 es:", sueldosAltos)
