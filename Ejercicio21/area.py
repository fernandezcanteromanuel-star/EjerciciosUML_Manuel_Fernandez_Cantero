from entidad_geografica import EntidadGeografica

class Area(EntidadGeografica):
    def __init__(self, nombre, codigo, puntos):
        super().__init__(nombre, codigo)
        if len(puntos) < 3:
            raise ValueError("Un área debe tener al menos 3 puntos.")
        self.puntos = puntos

    def mostrar_puntos(self):
        print(f"Área {self.nombre} formada por:")
        for p in self.puntos:
            print(f" - Punto {p.nombre} en {p.coordenadas()}")
