class Elipse:
    def __init__(self, eje_mayor, eje_menor, color):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color
    
    def __str__(self):
        return f"Elipse - Color: {self.color}, Eje Mayor: {self.eje_mayor}, Eje Menor: {self.eje_menor}"