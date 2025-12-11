from rol import Rol

class Responsable(Rol):
    def __init__(self, persona):
        super().__init__(persona)

    def dirigir_proyecto(self, proyecto):
        proyecto.responsables.append(self)
        print(f"{self.persona.nombre} ahora dirige el proyecto '{proyecto.nombre}'.")
