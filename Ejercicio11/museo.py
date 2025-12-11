class Museo:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.obras = []
    
    def agregar_obra(self, obra):
        self.obras.append(obra)
    
    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"