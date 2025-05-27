import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10) 
    intentos = 0
    max_intentos = 5

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10.")
    print(f"Tienes {max_intentos} intentos para adivinarlo.")

    while intentos < max_intentos:
        try:
            intento = int(input("Ingresa tu intento: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if intento < 1 or intento > 10:
            print("El número debe estar entre 1 y 10.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            return
        elif intento < numero_secreto:
            print("El número es más alto.")
        else:
            print("El número es más bajo.")

        print(f"Te quedan {max_intentos - intentos} intento(s).\n")

    print(f"Lo siento, se te acabaron los intentos. El número era {numero_secreto}.")

# Ejecutar el juego
adivina_el_numero()
