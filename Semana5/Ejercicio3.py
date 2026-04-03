'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''

monto = int(input("Ingrese el monto que desea retirar: "))
while monto == 0:
    monto = int(input("Ingrese un monto valido para retirar: "))
    while monto % 10 != 0:
        monto = int(input("Ingrese un monto valido para retirar: "))

print("Retiro exitoso")