from estructura import Estructura
from material import Material

if __name__ == '__main__':
    material1 = Material("Piedra", 60)
    material2 = Material("Arcilla", 30)
    material3 = Material("Arena", 10)
    
    subestructura1 = Estructura("EST-002", "Edad de Bronce")
    subestructura1.agregar_material(material1)
    
    subestructura2 = Estructura("EST-003", "Edad de Hierro")
    subestructura2.agregar_material(material2)
    
    estructura_principal = Estructura("EST-001", "Edad de Piedra")
    estructura_principal.agregar_material(material1)
    estructura_principal.agregar_material(material2)
    estructura_principal.agregar_material(material3)
    estructura_principal.agregar_subestructura(subestructura1)
    estructura_principal.agregar_subestructura(subestructura2)
    
    print("=== ESTRUCTURA PRINCIPAL ===")
    print(estructura_principal)
    
    print("\n=== SUBESTRUCTURAS ===")
    for subestructura in estructura_principal.subestructuras:
        print(subestructura)