from entidad_geografica import EntidadGeografica

class Linea(EntidadGeografica):
    def __init__(self, nombre, codigo, puntos):
        super().__init__(nombre, codigo)
        if len(puntos) < 2:
            raise ValueError("Una línea debe tener al menos 2 puntos.")
        self.puntos = puntos

    def mostrar_puntos(self):
        print(f"Línea {self.nombre} formada por:")
        for p in self.puntos:
            print(f" - Punto {p.nombre} en {p.coordenadas()}")
