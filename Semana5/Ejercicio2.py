'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
temp = int(input("Ingrese la temperatura: "))
if temp < 10:
    print("Fría")
elif 9 < temp < 26:
    print("Templada")
elif temp > 25:
    print("Calurosa") 