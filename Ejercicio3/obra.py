class Obra:
    def __init__(self, titulo, autor, año_inicio, año_fin, tecnica, material, descripcion, museo=None):
        self.titulo = titulo
        self.autor = autor
        self.año_inicio = año_inicio
        self.año_fin = año_fin
        self.tecnica = tecnica
        self.material = material
        self.descripcion = descripcion
        self.museo = museo
    
    def __str__(self):
        return f"Obra: {self.titulo} - Autor: {self.autor.nombre} ({self.año_inicio}-{self.año_fin}) - Material: {self.material} - Técnica: {self.tecnica}"