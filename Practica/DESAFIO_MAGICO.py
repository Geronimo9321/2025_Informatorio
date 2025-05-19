#Desafio Magico. En este desafio utilice. Algo de IA
#Ciclos While - For. Condicional if. Lista - Diccionario - Tupla - Import random.

print("---- DESAFÍO 1: El Guardián de los Nombres ----")

guardianes = ["nico", "marian", "guille"]
intentos = 0
max_intentos = 3

nombre_ingresado = input("Decí el nombre de un guardián secreto: ").strip().lower()

while nombre_ingresado not in guardianes and intentos < max_intentos - 1:
    intentos += 1
    print("Nombre incorrecto. Intentá nuevamente.")
    nombre_ingresado = input("Decí el nombre de un guardián secreto: ").strip().lower()

# Verificamos si logró acertar o no
if nombre_ingresado in guardianes:
    print("¡Correcto! El guardián te deja pasar.")
else:
    print("Fallaste 3 veces. ¡Quedaste atrapado!")
    exit()

# Preguntamos si quiere continuar al siguiente desafío
pasar_nivel = input("¿Querés pasar al Desafío 2? (si/no): ").strip().lower()
if pasar_nivel != "s":
    print("Te quedaste descansando. ¡Fin del juego!")
    exit()

print("----")

print("---- DESAFÍO 2: El Guardián de los Números ----")

numeros_magicos = [3, 12, 8, 7, 20]

# Contar cuántos son pares
pares = 0
for num in numeros_magicos:
    if num % 2 == 0:
        pares += 1

max_intentos = 3
intentos = 0

print("Debes adivinar cuántos números mágicos son pares.")
print("Ingresá un número entre 1 y 5.")

while intentos < max_intentos:
    try:
        respuesta = int(input("¿Cuántos números mágicos son pares? (1 a 5): "))
    except ValueError:
        print("Entrada no válida. Ingresá un número entre 1 y 5.")
        intentos += 1
        continue

    if respuesta < 1 or respuesta > 5:
        print("El número debe estar entre 1 y 5.")
        intentos += 1
        print(f"Te quedan {max_intentos - intentos} intentos.")
        continue

    if respuesta == pares:
        print("¡Correcto! El guardián te deja pasar.")
        break
    else:
        intentos += 1
        if intentos < max_intentos:
            print("Respuesta incorrecta. Intentá nuevamente.")
            print(f"Te quedan {max_intentos - intentos} intentos.\n")
        else:
            print("Fallaste 3 veces. ¡Quedaste atrapado!")
            print(f"La respuesta correcta era: {pares}")


# Preguntamos si quiere continuar al siguiente desafío
pasar_nivel = input("¿Querés pasar al Desafío 3? (si/no): ").strip().lower()
if pasar_nivel != "s":
    print("Te sentaste a contar cervezas mágicas. ¡Fin del juego!")
    exit()

print("----")

# DESAFÍO 3: El Guardián de los Datos
# Estructuras usadas: diccionario, tupla, ciclo while, condicional if, input

import random

print("---- DESAFÍO 3: El Guardián de los Datos ----")

animales = {
    "dragon": ("volar", "fuego", 500),
    "fenix": ("renacer", "luz", 1000),
    "unicorno": ("curar", "magia", 300)
}

# Mostrar pistas (habilidades) disponibles
print("El guardián te da pistas sobre animales mágicos...")
print("Pistas disponibles (habilidades):")
for datos in animales.values():
    print(f"- Este animal puede {datos[0]}")

# Elegir una habilidad al azar como pista
pista_elegida = random.choice([datos[0] for datos in animales.values()])

print(f"\nPista mágica: ¿Qué animal tiene la habilidad de '{pista_elegida}'?")

# Juego con intentos
intentos = 0
max_intentos = 3
acertado = False

while intentos < max_intentos:
    respuesta = input("Tu respuesta: ").strip().lower()
    if respuesta in animales:
        habilidad = animales[respuesta][0]
        if habilidad == pista_elegida:
            print(f"¡Correcto! El animal era {respuesta.capitalize()}")
            datos = animales[respuesta]
            print(f"- Habilidad: {datos[0]}")
            print(f"- Poder: {datos[1]}")
            print(f"- Edad: {datos[2]} años")
            print("¡Has pasado todos los desafíos!, ¡Ganaste el juego! 🏆")
            print("Bienvenido a la taberna querido viajero 🍻")
            acertado = True
            break
        else:
            print(f"No, {respuesta.capitalize()} no tiene la habilidad '{pista_elegida}'.")
    else:
        print("Ese animal no está en la lista mágica.")
    intentos += 1

if not acertado:
    print("Fallaste 3 veces. ¡Quedaste atrapado!")


    #print("¡Ganaste el juego! 🏆")
    #print("Bienvenido a la taberna querido viajero 🍻")
