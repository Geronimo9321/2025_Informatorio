num = int(input("Ingresar número: "))
print(f'Los divisores de {num} son: ')

for i in range(1, num + 1):
    if num % i == 0:
        print(i)