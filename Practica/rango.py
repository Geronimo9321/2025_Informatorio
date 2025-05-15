# Actividad número entre el rango de 10 y 50.

num = int(input("Ingresar un número: "))

if 10 <= num and num <= 50:
    print(f'El número ingresado: {num} esta en rango.')
else:
    print(f'El número ingresado: {num} esta fuera del rango.')