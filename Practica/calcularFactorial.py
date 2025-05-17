#Calcular el factorial de un número

numero = int(input("Ingresar número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f'El factorialde {numero} es: {factorial}')