class Lector:
    def __init__(self, id_identificacion, nombre, direccion):
        self.id_identificacion = id_identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.prestamos = []
        self.penalizacion = False
    
    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
    
    def __str__(self):
        return f"Lector: {self.nombre} | ID: {self.id_identificacion} | Dirección: {self.direccion}"