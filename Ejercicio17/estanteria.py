class Estanteria:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.libros = []
    
    def agregar_libro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            return True
        return False
    
    def __str__(self):
        return f"Estantería {self.numero} | Capacidad: {self.capacidad} | Libros: {len(self.libros)}"