class Obra:
    def __init__(self, titulo, artista, año_inicio, año_fin, tecnica, material, descripcion, museo):
        self.titulo = titulo
        self.artista = artista
        self.año_inicio = año_inicio
        self.año_fin = año_fin
        self.tecnica = tecnica
        self.material = material
        self.descripcion = descripcion
        self.museo = museo
        self.artista.agregar_obra(self)
        self.museo.agregar_obra(self)
    
    def __str__(self):
        return f"Obra: {self.titulo} - Autor: {self.artista.nombre} ({self.año_inicio}-{self.año_fin}) - Material: {self.material}"