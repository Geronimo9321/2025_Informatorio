n = int(input("Ingresar números: "))
suma = 0

for i in range(n):
    impar = 2 * i + 1
    suma += impar
print(f'La suma de los primeros {n} números impares es: {suma}')