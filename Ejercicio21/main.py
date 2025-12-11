from punto import Punto
from linea import Linea
from area import Area

if __name__ == "__main__":
    # Crear puntos
    p1 = Punto("P1", "001", 0, 0)
    p2 = Punto("P2", "002", 1, 1)
    p3 = Punto("P3", "003", 2, 0)

    # Crear línea con dos puntos
    linea1 = Linea("Línea A", "L001", [p1, p2])
    linea1.mostrar_puntos()

    # Crear área con tres puntos
    area1 = Area("Área X", "A001", [p1, p2, p3])
    area1.mostrar_puntos()
