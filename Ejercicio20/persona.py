class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.roles = []  # Una persona puede tener múltiples roles

    def agregar_rol(self, rol):
        self.roles.append(rol)

    def mostrar_roles(self):
        print(f"Persona: {self.nombre}")
        for rol in self.roles:
            print(f" - Rol: {rol.__class__.__name__}")
