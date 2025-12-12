from espacio import Espacio

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.espacios = []

    def agregar_espacio(self, espacio: Espacio):
        self.espacios.append(espacio)

    def mostrar_info(self):
        print(f"Ciudad: {self.nombre}")
        for espacio in self.espacios:
            espacio.mostrar_info()
