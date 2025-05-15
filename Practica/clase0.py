num = int(input("Ingresar un número: "))
num_impar = num
digitos = 0

while num != 0:
    num = num // 10
    digitos = digitos + 1 

print(f'La cantidad de digitos de {num_impar} es {digitos}')