from museo import Museo
from coleccion import Coleccion
from objeto_arqueologico import ObjetoArqueologico
from sala import Sala
from almacen import Almacen

if __name__ == "__main__":
    # Crear museo
    museo = Museo("Museo Nacional")

    # Crear colecciones
    coleccion1 = Coleccion("Colección Egipcia")

    # Crear ubicaciones
    sala1 = Sala("Sala Faraones", 2)
    almacen1 = Almacen("Almacén Principal")

    # Crear objetos arqueológicos
    objeto1 = ObjetoArqueologico("Sarcófago", sala1)
    objeto2 = ObjetoArqueologico("Vasija Antigua", almacen1)

    # Agregar objetos a la colección
    coleccion1.agregar_objeto(objeto1)
    coleccion1.agregar_objeto(objeto2)

    # Agregar colección al museo
    museo.agregar_coleccion(coleccion1)

    # Mostrar colecciones y objetos
    museo.mostrar_colecciones()
    coleccion1.mostrar_objetos()

    # Restauración
    objeto1.iniciar_restauracion()
    objeto1.finalizar_restauracion()
