class Libro:
    """
    Definición formal:
    Un Libro es un conjunto de hojas de papel manuscritas o impresas
    que, cosidas o encuadernadas, forman un volumen.
    """

    def __init__(self, hojas, encuadernado=True):
        self.hojas = hojas  # lista de hojas (texto manuscrito o impreso)
        self.encuadernado = encuadernado

    def es_volumen(self):
        # Invariante: debe estar encuadernado para ser considerado libro
        return self.encuadernado and len(self.hojas) > 0

    def mostrar_info(self):
        print(f"Libro con {len(self.hojas)} hojas, encuadernado: {self.encuadernado}")
