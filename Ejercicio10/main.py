from proyecto import Proyecto
from miembro import Miembro

if __name__ == '__main__':
    miembro1 = Miembro("Dr. Juan García", "Director", 15)
    miembro2 = Miembro("Dra. María López", "Investigadora", 10)
    miembro3 = Miembro("Carlos Ruiz", "Técnico", 5)
    
    proyecto = Proyecto(
        "Estudio del Movimiento de Órbitas Planetarias",
        "Investigación sobre las trayectorias de planetas",
        2023,
        "Modelar órbitas planetarias"
    )
    
    proyecto.agregar_miembro(miembro1)
    proyecto.agregar_miembro(miembro2)
    proyecto.agregar_miembro(miembro3)
    
    print(proyecto)
    print(f"\nMiembro 1 pertenece al proyecto: {miembro1.proyecto.nombre}")
    print(f"Miembro 2 pertenece al proyecto: {miembro2.proyecto.nombre}")