class Poligono:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
    
    def agregar_punto(self, punto):
        self.puntos.append(punto)
    
    def __str__(self):
        puntos_str = ", ".join([str(p) for p in self.puntos])
        return f"Polígono: {self.nombre} - Número de vértices: {len(self.puntos)}\nVértices: {puntos_str}"