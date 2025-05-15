#Cargar una lista con el nombre y la edad de todos los participantes del informatorio.

participantes = []

cantidad = int(input("¿Cuántos participantes quieres ingresar? "))

for i in range(cantidad):
    print(f"\nParticipante {i + 1}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    participante = {"nombre": nombre, "apellido": apellido, "edad": edad}
    participantes.append(participante)

print("\nLista de participantes:")
for p in participantes:
    print(f"Datos del participante. Nombre: {p['nombre']}, Apellido: {p['apellido']} Edad: {p['edad']}")
