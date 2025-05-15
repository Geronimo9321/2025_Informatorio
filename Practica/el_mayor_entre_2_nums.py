# En el if voy a comparar si el primer número es el mayor que el segundo núm.
# En el elif voy a comparar si el segundo número es el mayor que el primer núm.
# En el else voy a comparar si los números son iguales.

num_1 = int(input("Ingresar un número: "))
num_2 = int(input("Ingresar otro número: "))

if num_1 > num_2:
    print(f'El {num_1} es mayor al', num_2)
elif num_2 > num_1:
    print(f'El {num_2} es mayor al', num_1)
else:
    print("Ambos números son iguales.")