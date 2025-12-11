class ProyectoArqueologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.actuaciones = []
        self.responsables = []
        self.tecnicos = []

    def agregar_actuacion(self, actuacion):
        self.actuaciones.append(actuacion)

    def mostrar_info(self):
        print(f"Proyecto: {self.nombre}")
        print(" Responsables:")
        for r in self.responsables:
            print(f"  - {r.persona.nombre}")
        print(" Técnicos:")
        for t in self.tecnicos:
            print(f"  - {t.persona.nombre}")
        print(" Actuaciones:")
        for a in self.actuaciones:
            print(f"  - {a.nombre}")
