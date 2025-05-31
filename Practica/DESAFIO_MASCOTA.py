# DESAFÍO MASCOTA

class Mascota:

    def __init__(self, nombre, edad, especie, energia):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.energia = 100  

    # GET & SET
    def setNombre(self, new):
        self.nombre = new

    def getNombre(self):
        return self.nombre

    def setEdad(self, new):
        self.edad = new

    def getEdad(self):
        return self.edad

    def setEspecie(self, new):
        self.especie = new

    def getEspecie(self):
        return self.especie

    def setEnergia(self, new):
        nueva_energia = self.energia - (new * 10)
        self.energia = max(nueva_energia, 0)

    def getEnergia(self):
        return self.energia

    # OTROS MÉTODOS
    def saludar(self):
        return f'¡Hola! Soy {self.nombre}, un {self.especie} feliz.'

    def comer(self, comida):
        return f'{self.nombre} está comiendo {comida}.'

    def cumplir_anios(self):
        nueva_edad = self.edad + 1
        self.setEdad(nueva_edad)
        return f'¡{self.nombre} ahora tiene {self.getEdad()} años!'

    def jugar(self, tiempo):
        self.setEnergia(tiempo)
        if self.energia > 0:
            return f'{self.nombre} jugó {tiempo} minuto(s) y tiene {self.energia} de energía.'
        else:
            return f'¡{self.nombre} está muy cansad@!'

    def descansar(self, tiempo):
        self.energia += tiempo * 5
        if self.energia > 100:
            self.energia = 100
        return f'{self.nombre} descansó y recuperó energía. Ahora tiene {self.energia}.'

    def estado(self):
        return f'Estado de {self.nombre}: Edad = {self.edad}, Especie = {self.especie}, Energía = {self.energia}'


# Crear mascotas 
m_1 = Mascota('Lara', 9, 'perro', 100)
m_2 = Mascota('Antonio', 7, 'gato', 100)
m_3 = Mascota('Nemo', 3, 'pez', 100)
m_4 = Mascota('Donatelo', 14, 'tortuga', 100)
m_5 = Mascota('Pana', 2, 'conejo', 100)

# Pruebas individuales
print(' Pruebas individuales:\n')
print(m_1.saludar())
print(m_2.comer('alimento balanceado'))
print(m_3.cumplir_anios())
print(m_4.jugar(5))
print(m_5.jugar(10))
print(m_5.descansar(4))
print(m_5.estado())

# Desafío Extra
print('\n Desafío Extra:\n')
mascotas = [m_1, m_2, m_3]
for mascota in mascotas:
    print(mascota.saludar())
    print(mascota.comer("zanahorias mágicas"))
    print(mascota.jugar(3))
    print(mascota.descansar(2))
    print(mascota.cumplir_anios())
    print(mascota.estado())
    print("-" * 40)
