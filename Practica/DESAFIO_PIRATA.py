#MI DESAFIO PIRATA

import random

def generar_halago(*args, **kwargs):
    #LISTA POR DEFECTO
    comienzos = kwargs.get("comienzos", ["Oh noble", "Capitana de mi alma", "Estrella de mi brújula", "Tesoro de los siete mares"])
    adjetivos = kwargs.get("adjetivos", ["sirena encantadora", "joya marina", "faro de mi corazón", "ola de dulzura", "brisa de ternura"])

    if args:
        adjetivos.extend(args)
    
    #OPCIONES DECORATIVAS
    emoji = kwargs.get("emoji", "💖")
    separador = kwargs.get("separador", "~")

    #FRASES AL AZAR
    inicio = random.choice(comienzos)
    medio = random.choice(adjetivos)
    return f'{inicio}{separador}{medio} {emoji}'

    #INTERACCION CON EL USUARIO
def modo_romance_pirata():
    print("⚓ Bienvenido al generador de halagos del Pirata Sin Palabras ⚓")
    nombre_sirena = input("¿Cómo se llama la sirena que ha robado el corazón del pirata?\n")

    while True:
        cantidad = input(f"¿Cuantos halagos quiere dedicarle el pirata a {nombre_sirena}? (o escribe 'basta' para salir): ")

        if cantidad.lower() == "basta":
            print("El pirata se retira con el corazón lleno de esperanza... 🌊")
            break
            
        if not cantidad.isdigit():
            print("⚠️ Por favor, escribe un número válido o 'basta'.")
            continue
            
        cantidad = int(cantidad)
        print(f"\n🌺 Aquí van {cantidad} halagos para {nombre_sirena}:\n")
        for _ in range(cantidad):
            print(generar_halago("reina del horizonte", "encantadora de mares", emoji="🏴‍☠️", separador=" ♥ "))
        print("\n✨ ¿Deseas enviar más halagos o decir 'basta'?")
            
modo_romance_pirata()
