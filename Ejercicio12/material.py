class Material:
    def __init__(self, nombre, porcentaje):
        self.nombre = nombre
        self.porcentaje = porcentaje
    
    def __str__(self):
        return f"{self.nombre} ({self.porcentaje}%)"