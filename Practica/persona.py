class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrarInfo(self):
        return f'{self.nombre}, {self.edad} años, DNI: {self.dni}'

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera

    def mostrarInfo(self):
        return f'Estudiante: {super().mostrarInfo()}, Carrera: {self.carrera}'

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, materia):
        super().__init__(nombre, edad, dni)
        self.materia = materia

    def mostrarInfo(self):
        return f'Profesor: {super().mostrarInfo()}, Materia: {self.materia}'

e1 = Estudiante("Geronimo", 29, "13420953", "POO")
p1 = Profesor("Nicolas", 35, "1234098", "Python")

print(e1.mostrarInfo())
print(p1.mostrarInfo())
