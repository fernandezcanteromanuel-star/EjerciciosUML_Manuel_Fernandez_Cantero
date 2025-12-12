from edificio import Edificio

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio: Edificio):
        self.edificios.append(edificio)

    def mostrar_info(self):
        print(f"Espacio: {self.nombre}")
        for edificio in self.edificios:
            edificio.mostrar_info()

class Calle(Espacio):
    def __init__(self, nombre, longitud):
        super().__init__(nombre)
        self.longitud = longitud

    def mostrar_info(self):
        print(f"Calle: {self.nombre}, longitud: {self.longitud} m")
        super().mostrar_info()

class Plaza(Espacio):
    def __init__(self, nombre, superficie):
        super().__init__(nombre)
        self.superficie = superficie

    def mostrar_info(self):
        print(f"Plaza: {self.nombre}, superficie: {self.superficie} m²")
        super().mostrar_info()
