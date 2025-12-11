class Catedral:
    def __init__(self, nombre, ciudad, provincia, pais, material, año_inicio, año_fin, año_consagracion, bien_interes_cultural):
        self.nombre = nombre
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
        self.material = material
        self.año_inicio = año_inicio
        self.año_fin = año_fin
        self.año_consagracion = año_consagracion
        self.bien_interes_cultural = bien_interes_cultural
        self.estilos = []
    
    def agregar_estilo(self, estilo):
        self.estilos.append(estilo)
    
    def __str__(self):
        estilos_str = ", ".join([str(e) for e in self.estilos])
        return f"Catedral: {self.nombre} - {self.ciudad}, {self.provincia} ({self.pais}) - Material: {self.material} - Construcción: {self.año_inicio}-{self.año_fin} - Consagración: {self.año_consagracion} - Estilos: {estilos_str}"