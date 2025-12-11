from proyecto import Proyecto
from miembro import Miembro

if __name__ == '__main__':
    miembro1 = Miembro("Dr. Juan García", "Director", 15)
    miembro2 = Miembro("Dra. María López", "Investigadora", 10)
    miembro3 = Miembro("Carlos Ruiz", "Técnico", 5)
    miembro4 = Miembro("Ana Martínez", "Investigadora", 3)
    
    proyecto = Proyecto(
        "Estudio del Movimiento de Órbitas Planetarias",
        "Investigación sobre las trayectorias de planetas utilizando ecuaciones de mecánica celeste",
        2023,
        "Modelar y predecir órbitas planetarias con precisión"
    )
    
    proyecto.agregar_miembro(miembro1)
    proyecto.agregar_miembro(miembro2)
    proyecto.agregar_miembro(miembro3)
    proyecto.agregar_miembro(miembro4)
    
    print(proyecto)
    print(f"\nTotal de miembros: {len(proyecto.miembros)}")