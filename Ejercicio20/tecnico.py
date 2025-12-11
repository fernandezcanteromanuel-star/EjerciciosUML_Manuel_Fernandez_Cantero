from rol import Rol

class Tecnico(Rol):
    def __init__(self, persona):
        super().__init__(persona)

    def participar_proyecto(self, proyecto):
        proyecto.tecnicos.append(self)
        print(f"{self.persona.nombre} participa en el proyecto '{proyecto.nombre}'.")

    def participar_actuacion(self, actuacion):
        actuacion.tecnicos.append(self)
        print(f"{self.persona.nombre} participa en la actuación '{actuacion.nombre}'.")
