while True:
    entrada = input("Ingresar un número (o escribe SALIR para terminar.): ")

    if entrada.lower() == "salir":
        print("Programa Finalizado.")
        break

    try:
        numero = float(entrada)
        print(f'Ingresaste el número: {numero}')
    except ValueError:
        print("Eso no es un número válido. Intentalo otra vez.")