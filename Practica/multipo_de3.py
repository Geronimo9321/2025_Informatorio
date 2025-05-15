#Ejercicio núm 5: verificar si el núm ingresado es multiplo de 3

num = int(input("Ingresar el número: "))

if num % 3 == 0:
    print(f'Este número {num}, SI es múltiplo de 3.')
else:
    print(f'Este número {num}, NO es múltiplo de 3.')