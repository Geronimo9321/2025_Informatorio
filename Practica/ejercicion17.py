#LA TABLA DE MULTIPLICAR DE UN NÚMERO DADO:

numero = int(input("Ingresar un número para ver su tabla de multiplicar: "))
i = 1

while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i += 1
    