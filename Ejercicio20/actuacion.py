class Actuacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tecnicos = []

    def mostrar_tecnicos(self):
        print(f"Actuación: {self.nombre}")
        for t in self.tecnicos:
            print(f" - Técnico: {t.persona.nombre}")
