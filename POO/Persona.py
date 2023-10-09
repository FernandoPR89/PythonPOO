class Persona:
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad

    def valores(self):
        print(f'Nombre {self.Nombre}\nEdad:{self.Edad}')
