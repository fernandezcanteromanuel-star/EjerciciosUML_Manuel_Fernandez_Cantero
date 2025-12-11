class Prestamo:
    def __init__(self, libro, fecha_prestamo, fecha_entrega, usuario):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.usuario = usuario
        self.plazo_maximo = 30
    
    def __str__(self):
        return f"Libro: {self.libro.titulo} | Prestado a: {self.usuario.nombre} | Prestamo: {self.fecha_prestamo} | Entrega: {self.fecha_entrega}"