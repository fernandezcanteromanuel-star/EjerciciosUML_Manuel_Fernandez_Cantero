class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.obras = []
    
    def agregar_obra(self, obra):
        self.obras.append(obra)
    
    def __str__(self):
        return f"{self.nombre}"