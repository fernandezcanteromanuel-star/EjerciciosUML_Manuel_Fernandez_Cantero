class Persona:
    def __init__(self, nombre, apellido1, apellido2, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion
        self.conyuge = None
        self.padre = None
        self.madre = None
        self.hijos = []
    
    def casarse(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self
    
    def set_padre(self, padre):
        self.padre = padre
        if self not in padre.hijos:
            padre.hijos.append(self)
    
    def set_madre(self, madre):
        self.madre = madre
        if self not in madre.hijos:
            madre.hijos.append(self)
    
    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
    
    def __str__(self):
        info = f"{self.nombre} {self.apellido1} {self.apellido2}"
        info += f"\nID: {self.numero_identificacion} | Sexo: {self.sexo} | Nacimiento: {self.fecha_nacimiento}"
        
        if self.conyuge:
            info += f"\nCónyuge: {self.conyuge.nombre} {self.conyuge.apellido1}"
        
        if self.padre or self.madre:
            padres = []
            if self.padre:
                padres.append(f"Padre: {self.padre.nombre}")
            if self.madre:
                padres.append(f"Madre: {self.madre.nombre}")
            info += f"\n{', '.join(padres)}"
        
        if self.hijos:
            hijos_str = ", ".join([f"{h.nombre}" for h in self.hijos])
            info += f"\nHijos: {hijos_str}"
        
        return info