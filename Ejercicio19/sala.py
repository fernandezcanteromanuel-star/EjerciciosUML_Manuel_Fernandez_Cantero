class Sala:
    def __init__(self, nombre, piso):
        self.nombre = nombre
        self.piso = piso

    def __str__(self):
        return f"Sala {self.nombre}, Piso {self.piso}"
