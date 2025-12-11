class Museo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.colecciones = []

    def agregar_coleccion(self, coleccion):
        self.colecciones.append(coleccion)

    def mostrar_colecciones(self):
        for c in self.colecciones:
            print(f"Colección: {c.nombre}")
