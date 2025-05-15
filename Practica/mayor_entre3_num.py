num1 = int(input("Ingresar un número aleatorio: "))
num2 = int(input("Ingresar un número aleatorio: "))
num3 = int(input("Ingresar un número aleatorio: "))

if num1 >= num2 and num1 >= num3:
    print("El número mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El número mayor es:", num2)
else:
    print("El número mayor es:", num3)