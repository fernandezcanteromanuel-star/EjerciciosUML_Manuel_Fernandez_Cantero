from entidad_geografica import EntidadGeografica

class Punto(EntidadGeografica):
    def __init__(self, nombre, codigo, x, y):
        super().__init__(nombre, codigo)
        self.x = x
        self.y = y

    def coordenadas(self):
        return (self.x, self.y)
