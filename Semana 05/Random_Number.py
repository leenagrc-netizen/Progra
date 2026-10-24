

# Esta indicacion le dice a Python que trabaje con una herramienta que genera numeros aleatorios

import random

numero_secreto = random.randint(1,20)
intentos = 0

while True:
    intentos = intentos + 1
    intento = int(input("Ingrese un numero: "))

    distancia = abs(numero_secreto - intento)

    if numero_secreto == intento:
        print(f"Has adivinado el numero en {intentos} intentos!")
        break

    elif numero_secreto > intento:
        print("El numero secreto es mayor al numero digitado! Intente de nuevo")

    else:
        print("El numero secreto es menor al numero digitado! Intente de nuevo")

    if distancia <= 2:
        print("Hirviendo!")

    elif distancia <= 5:
        print("Caliente!")

    elif distancia <= 10:
        print("Tibio!")

    else:
        print("Frio!")