class Rectangulo:
    def __init__(self, anchura, longitud, color):
        self.anchura = anchura
        self.longitud = longitud
        self.color = color
    
    def __str__(self):
        return f"Rectángulo - Color: {self.color}, Anchura: {self.anchura}, Longitud: {self.longitud}"