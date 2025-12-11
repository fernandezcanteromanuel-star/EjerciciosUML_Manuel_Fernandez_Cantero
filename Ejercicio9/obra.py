class Obra:
    def __init__(self, titulo, pintor, representacion, ubicacion, tiene_copias, tecnica, material, sub_tecnica, estado_conservacion):
        self.titulo = titulo
        self.pintor = pintor
        self.representacion = representacion
        self.ubicacion = ubicacion
        self.tiene_copias = tiene_copias
        self.tecnica = tecnica
        self.material = material
        self.sub_tecnica = sub_tecnica
        self.estado_conservacion = estado_conservacion
    
    def __str__(self):
        return f"Obra: {self.titulo}\nPintor: {self.pintor}\nRepresentación: {self.representacion}\nUbicación: {self.ubicacion}\nTiene copias: {self.tiene_copias}\nTécnica: {self.tecnica}\nMaterial: {self.material}\nSub-técnica: {self.sub_tecnica}\nEstado de conservación: {self.estado_conservacion}"