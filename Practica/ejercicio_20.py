contador = 0
numero = int(input("Ingresar número: "))

while numero != -1:
    if numero > 50:
        contador += 1
    numero = int(input("Ingresar otro número, o agregar un -1 para salir: "))

print(f'Se ingresarón {contador} números mayores a 50.')
