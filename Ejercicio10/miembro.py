class Miembro:
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia
        self.proyecto = None
    
    def __str__(self):
        return f"{self.nombre} - Rol: {self.rol}, Experiencia: {self.experiencia} años"