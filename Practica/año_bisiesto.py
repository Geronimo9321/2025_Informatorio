año = int(input("Ingresar año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f'El año {año} SI es bisiesto.')
else:
    print(f'El año {año} NO es bisiesto.')