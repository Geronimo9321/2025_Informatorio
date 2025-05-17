palabra = input("Ingresar una palabra: ")
contador = 0

for letra in palabra:
    if letra == "a":
        contador += 1
print(f'La letra {letra} aparace, {contador} veces en la palabra.')