class Estructura:
    def __init__(self, codigo, datacion):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = []
        self.subestructuras = []
    
    def agregar_material(self, material):
        self.materiales.append(material)
    
    def agregar_subestructura(self, estructura):
        self.subestructuras.append(estructura)
    
    def __str__(self):
        materiales_str = ", ".join([str(m) for m in self.materiales])
        subestructuras_str = ", ".join([e.codigo for e in self.subestructuras])
        return f"Estructura: {self.codigo} - Datación: {self.datacion}\nMateriales: {materiales_str}\nSubestructuras: {subestructuras_str if subestructuras_str else 'Ninguna'}"