class Muestra:
    """
    Definición formal:
    Una Muestra es una parte o porción extraída de un conjunto,
    por métodos que permiten considerarla representativa del mismo.
    """

    def __init__(self, porcion, conjunto, representativa=True):
        self.porcion = porcion  # parte extraída
        self.conjunto = conjunto  # conjunto original
        self.representativa = representativa

    def es_valida(self):
        # Invariante: debe ser representativa y provenir de un conjunto
        return self.representativa and self.conjunto is not None

    def mostrar_info(self):
        print(f"Muestra de {self.porcion} extraída de {self.conjunto}, representativa: {self.representativa}")
