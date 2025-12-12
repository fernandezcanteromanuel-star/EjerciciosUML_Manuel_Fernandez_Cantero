from fachada import Fachada

class Edificio:
    def __init__(self, nombre, pisos):
        self.nombre = nombre
        self.pisos = pisos
        self.fachada = None

    def agregar_fachada(self, fachada: Fachada):
        self.fachada = fachada

    def mostrar_info(self):
        print(f"Edificio: {self.nombre}, pisos: {self.pisos}")
        if self.fachada:
            self.fachada.mostrar_info()
