from figura import Figura

class Rectangulo(Figura):
    def __init__(self, anchura, longitud, color):
        super().__init__(color)
        self.anchura = anchura
        self.longitud = longitud
    
    def __str__(self):
        return f"Rectángulo - Color: {self.color}, Anchura: {self.anchura}, Longitud: {self.longitud}"