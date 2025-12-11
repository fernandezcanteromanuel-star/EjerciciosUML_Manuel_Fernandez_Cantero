class Poligono:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
        for punto in puntos:
            punto.agregar_poligono(self)
    
    def agregar_punto(self, punto):
        self.puntos.append(punto)
        punto.agregar_poligono(self)
    
    def __str__(self):
        puntos_str = ", ".join([str(p) for p in self.puntos])
        return f"Polígono: {self.nombre} - Número de vértices: {len(self.puntos)}\nVértices: {puntos_str}"