class Planta:
    def __init__(self, numero):
        self.numero = numero
        self.estanterias = []
    
    def agregar_estanteria(self, estanteria):
        self.estanterias.append(estanteria)
    
    def __str__(self):
        estanterias_str = ", ".join([str(e) for e in self.estanterias])
        return f"Planta {self.numero} | Estanterías: {estanterias_str}"