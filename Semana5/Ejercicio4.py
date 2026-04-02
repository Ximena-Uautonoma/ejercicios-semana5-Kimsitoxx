'''Registro de asistencia diaria
En una oficina se registra la asistencia hasta que el trabajador ingresa 0.
Solicita repetidamente:
1 si asistió
0 para terminar
Al final, muestra cuántos días asistió.'''

si = 1
asistencia = 0
while si == 1:
    si = int(input("Confirme asistencia del dia de hoy (1 Si, 0 No): "))
    if si == 1:
        asistencia = asistencia + 1

print("Asistió", asistencia, "dias.")