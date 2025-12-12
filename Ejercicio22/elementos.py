class ElementoArquitectonico:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def mostrar_info(self):
        print(f"Elemento: {self.nombre}, material: {self.material}")

class Portada(ElementoArquitectonico):
    def __init__(self, material, decoracion):
        super().__init__("Portada", material)
        self.decoracion = decoracion

    def mostrar_info(self):
        print(f"Portada de {self.material}, decoracion: {self.decoracion}")

class Puerta(ElementoArquitectonico):
    def __init__(self, material, tipo):
        super().__init__("Puerta", material)
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Puerta de {self.material}, tipo: {self.tipo}")

class Ventana(ElementoArquitectonico):
    def __init__(self, material, forma):
        super().__init__("Ventana", material)
        self.forma = forma

    def mostrar_info(self):
        print(f"Ventana de {self.material}, forma: {self.forma}")

class Balcon(ElementoArquitectonico):
    def __init__(self, material, tamaño):
        super().__init__("Balcón", material)
        self.tamaño = tamaño

    def mostrar_info(self):
        print(f"Balcón de {self.material}, tamaño: {self.tamaño} m²")
