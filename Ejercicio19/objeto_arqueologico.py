class ObjetoArqueologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.en_restauracion = False

    def iniciar_restauracion(self):
        self.en_restauracion = True
        print(f"El objeto '{self.nombre}' está en restauración.")

    def finalizar_restauracion(self):
        self.en_restauracion = False
        print(f"El objeto '{self.nombre}' ha sido restaurado.")
