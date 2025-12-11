from punto import Punto
from poligono import Poligono

if __name__ == '__main__':
    punto1 = Punto(0, 0)
    punto2 = Punto(4, 0)
    punto3 = Punto(4, 3)
    punto4 = Punto(0, 3)
    
    rectangulo = Poligono("Rectángulo", [punto1, punto2, punto3, punto4])
    
    punto5 = Punto(0, 0)
    punto6 = Punto(3, 0)
    punto7 = Punto(1.5, 2.6)
    
    triangulo = Poligono("Triángulo", [punto5, punto6, punto7])
    
    punto8 = Punto(2, 0)
    punto9 = Punto(4, 1)
    punto10 = Punto(4, 3)
    punto11 = Punto(2, 4)
    punto12 = Punto(0, 3)
    punto13 = Punto(0, 1)
    
    hexagono = Poligono("Hexágono", [punto8, punto9, punto10, punto11, punto12, punto13])
    
    print(rectangulo)
    print("\n" + str(triangulo))
    print("\n" + str(hexagono))