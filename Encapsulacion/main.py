from Encapsulacion.Ejemplo import Ejemplo
if __name__ == '__main__':

    ejemplo = Ejemplo()
    print(ejemplo.publico())
    #print(ejemplo.__privado())
    print(ejemplo._Ejemplo__privado()) # Name mangling permite el acceos a variable privadas
    print(ejemplo.get_oculto())