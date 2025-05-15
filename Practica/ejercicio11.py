#Empiezo la suma en 0.

suma = 0

num = int(input("Ingresar un número aleatorio: "))

#En el input del while le doy una opción para terminar el bucle

while num != 0:
    suma += num
    num = int(input("Agregue otro número. O presione 0 para salir: "))

#Muestro el resultado que se hizo hasta antes del 0.
print(f'La suma total fue: {suma}')