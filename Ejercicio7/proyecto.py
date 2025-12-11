class Proyecto:
    def __init__(self, nombre, descripcion, año_inicio, objetivo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.año_inicio = año_inicio
        self.objetivo = objetivo
        self.miembros = []
    
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
    
    def __str__(self):
        miembros_str = ", ".join([m.nombre for m in self.miembros])
        return f"Proyecto: {self.nombre}\nDescripción: {self.descripcion}\nAño inicio: {self.año_inicio}\nObjetivo: {self.objetivo}\nMiembros: {miembros_str}"