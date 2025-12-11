from figura import Figura

class Cuadrado(Figura):
    def __init__(self, longitud, color):
        super().__init__(color)
        self.longitud = longitud
    
    def __str__(self):
        return f"Cuadrado - Color: {self.color}, Longitud: {self.longitud}"