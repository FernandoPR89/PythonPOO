class Ejemplo:
    def __init__(self):
        self.__oculto="Variable oculta" #Variable privada

    def publico(self):
        return "Soy un metodo publico"

    def __privado(self): # Metodo privado
        return "Soy un metodo privado"

    def get_oculto(self):
        return self.__oculto
