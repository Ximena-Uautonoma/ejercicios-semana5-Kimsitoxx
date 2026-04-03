'''#Realice un ejercicio que permita la validación de contraseña simple
#La contraseña correcta es "abc123".
#Tarea
#Solicita la contraseña al usuario hasta que sea correcta
# si la contraseña es correcta muestra "Acceso concedido".
# sino muestra "Contraseña incorrecta, ingrese contraseña nuevamente por favor."
'''

contraseña = "1234"
entrada = "si"
while contraseña != entrada:
    entrada = input("Ingrese su contraseña: ")
    print("Contraseña incorrecta, ingrese contraseña nuevamente")

print("Contraseña correcta")