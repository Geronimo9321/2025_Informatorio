#Ejercicio número 4.
#Leer la edad ingresada y responder si es mayor o menor de edad.
#Uso >= para comparar la edad.

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(f'Tenes {edad} años, ya sos mayor.')
else:
    print(f'Tenes {edad} años, sos menor.')