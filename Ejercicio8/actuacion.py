class Actuacion:
    def __init__(self, fecha_inicio, fecha_fin, tipo):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo
    
    def __str__(self):
        return f"Actuación Arqueológica - Tipo: {self.tipo}, Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}"