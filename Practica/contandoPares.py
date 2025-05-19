numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_pares = []

for num in numeros:
    if num % 2 == 0:
        numero_pares.append(num)

print(f'Lista completa: {numeros}')
print(f'Esta es la cantidad de pares en la lista; ', len(numero_pares))
print(f'Los números pares encontrados son: {numero_pares}')
