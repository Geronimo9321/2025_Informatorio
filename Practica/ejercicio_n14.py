contador = 0

while True:
    numero = int(input("Ingresar un número. Para finalizar ingrese un número negativo(-1): "))
    if numero < 0:
        break
    contador += 1
print(f'Se ingresaron {contador}, números.')