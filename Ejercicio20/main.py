from persona import Persona
from responsable import Responsable
from tecnico import Tecnico
from proyecto import ProyectoArqueologico
from actuacion import Actuacion

if __name__ == "__main__":
    # Crear personas
    juan = Persona("Juan")
    maria = Persona("María")

    # Asignar roles
    rol_responsable = Responsable(juan)
    rol_tecnico = Tecnico(maria)

    juan.agregar_rol(rol_responsable)
    maria.agregar_rol(rol_tecnico)

    # Crear proyecto
    proyecto1 = ProyectoArqueologico("Excavación en Egipto")

    # Crear actuaciones
    actuacion1 = Actuacion("Excavación tumba faraónica")
    actuacion2 = Actuacion("Catalogación de piezas")

    proyecto1.agregar_actuacion(actuacion1)
    proyecto1.agregar_actuacion(actuacion2)

    # Vincular roles con proyecto y actuaciones
    rol_responsable.dirigir_proyecto(proyecto1)
    rol_tecnico.participar_proyecto(proyecto1)
    rol_tecnico.participar_actuacion(actuacion1)

    # Mostrar información
    proyecto1.mostrar_info()
    actuacion1.mostrar_tecnicos()
