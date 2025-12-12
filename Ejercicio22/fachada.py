from elementos import ElementoArquitectonico

class Fachada:
    def __init__(self, estilo):
        self.estilo = estilo
        self.elementos = []

    def agregar_elemento(self, elemento: ElementoArquitectonico):
        self.elementos.append(elemento)

    def mostrar_info(self):
        print(f"Fachada estilo: {self.estilo}")
        for elemento in self.elementos:
            elemento.mostrar_info()
