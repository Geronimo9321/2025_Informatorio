#EL NÚMERO SECRETO ES EL 25
#ESTA EN EL RANGO DEL 1 AL 100
#SOLO 5 INTENTOS PERMITIDOS

num_secreto = 25
maximos_intentos = 5
intentos = 0

print("¡Adivina el número secreto entre el 1 y 100!")
print(f'Tienes {maximos_intentos} intentos.')

while intentos < maximos_intentos:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    intentos_restantes = maximos_intentos - intentos

    if intento == num_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break

    elif intento < num_secreto:
        print("El número secreto es mayor.")

    else:
        print("El número secreto es menor.")

    if intentos < maximos_intentos:
        print(f'Te quedan {intentos_restantes} intentos.')
    
if intento != num_secreto:
    print("Lo siento, se terminaron tus intentos.")
    print(f'El número secreto era: {num_secreto}.')