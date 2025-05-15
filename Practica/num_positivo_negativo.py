# Voy a empezar desde el número 0
# Si el número ingresado es mayor a 0 son positivos.
# Si el número ingresado es menor a 0 seran los negativos.
# ¿Porque si ingreso el número en decimal me toma como positivo?

num = 0
num = float(input("Ingresar un número: "))

if num > 0:
    print("El número que ingreso es positivo.")
elif num < 0:
    print("El número que ingreso es negativo") 
else:
    print("El número que ingreso es cero.")