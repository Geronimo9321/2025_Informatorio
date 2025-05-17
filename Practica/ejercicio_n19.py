numero = int(input("Ingresar un número: "))
 
if numero % 2 != 0:
    print("Error. Solo debe ingresar números pares.")
else:
    i = 2
    while i <= numero:
        print(i)
        i += 2
        