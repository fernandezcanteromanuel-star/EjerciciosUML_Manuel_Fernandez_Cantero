class Empleado:
    def __init__(self, id_empleado, nombre, direccion):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.prestamos = []
    
    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
    
    def __str__(self):
        return f"Empleado: {self.nombre} | ID: {self.id_empleado} | Dirección: {self.direccion}"