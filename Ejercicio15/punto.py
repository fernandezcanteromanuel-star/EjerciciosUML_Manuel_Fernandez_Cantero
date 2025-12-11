class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligonos = []
    
    def agregar_poligono(self, poligono):
        if poligono not in self.poligonos:
            self.poligonos.append(poligono)
    
    def __str__(self):
        return f"({self.x}, {self.y})"