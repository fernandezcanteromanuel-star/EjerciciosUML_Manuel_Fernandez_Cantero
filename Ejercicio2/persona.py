class Persona:
    def __init__(self, nombre, apellido, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.conyuge = None
        self.padre = None
        self.madre = None
    
    def casarse(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self
    
    def set_padre(self, padre):
        self.padre = padre
    
    def set_madre(self, madre):
        self.madre = madre
    
    def __str__(self):
        info = f"{self.nombre} {self.apellido}"
        if self.apellido_nacimiento:
            info += f" (nacida {self.apellido_nacimiento})"
        return info