#contraseña correcta.

mi_contraseña = "gero1234"

contraseña_ingresada = input("Ingresar la contraseña: ")

while contraseña_ingresada != mi_contraseña:
    print("Contraseña incorrecta. Intenta nuevamente.")
    contraseña_ingresada = input("Ingresar la contraseña: ")

#Mensaje para la contraseña correcta
print("¡Bienvenido!")