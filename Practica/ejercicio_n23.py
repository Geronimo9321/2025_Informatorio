#Contar cuántos múltiplos de 3 hay del 1 al 100

contador = 0

for numero in range(1, 101):
    if numero % 3 == 0:
        contador += 1
print("La cantidad de múltiplos de 3 del 1 al 100 son:", contador)