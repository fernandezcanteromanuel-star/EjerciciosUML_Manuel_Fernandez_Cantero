class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def mostrar_objetos(self):
        for o in self.objetos:
            print(f"Objeto: {o.nombre}, Ubicación: {o.ubicacion}")
