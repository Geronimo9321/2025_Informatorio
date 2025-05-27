#como hacer una calculadora con funciones en python

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b 
def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b 
def potencia(a, b):
    return a ** b 
def raiz(a):
    if a < 0:
        return "No se puede calcular la raiz cuadrada de un número negativo"
    else:
        return a ** 0.5

def menu():
    print("Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

def calculadora(opcion):
    if opcion == 1:
        a = int(input("Ingresar un número: "))
        b = int(input("Ingresar otro número: "))
        print(f'La suma de {a} + {b} es {suma(a, b)}')
    elif opcion == 2: 
        a = int(input("Ingresar un número: "))
        b = int(input("Ingresar otro número: "))
        print(f'La resta de {a} - {b} es {resta(a, b)}')
    elif opcion == 3:
        a = int(input("Ingresar un número: "))
        b = int(input("Ingresar otro número: "))
        print(f'La multiplicación de {a} * {b} es {multiplicacion(a, b)}')
    elif opcion == 4:
        a = int(input("Ingresar un número: "))
        b = int(input("Ingresar otro número: "))
        print(f'La división de {a} / {b} es {division(a, b)}')
    elif opcion == 5:
        a = int(input("Ingresar un número: "))
        b = int(input("Ingresar otro número: "))
        print(f'La potencia de {a} ^ {b} es {potencia(a, b)}')
    elif opcion == 6:
        a = int(input("Ingresar un número: "))
        print(f'La raíz cuadrada de {a} es {raiz(a)}')
    else:
        print("Opción no válida")

opcion = menu()
while opcion != 7:
    calculadora(opcion)
    opcion = menu()

print("Gracias por usar la calculadora.")