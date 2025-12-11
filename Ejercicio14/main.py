from punto import Punto
from poligono import Poligono

if __name__ == '__main__':
    # Puntos comunes (lado compartido)
    puntoA = Punto(0, 0)
    puntoB = Punto(3, 0)
    
    # Punto único del triángulo 1
    puntoC = Punto(1.5, 2.6)
    
    # Punto único del triángulo 2
    puntoD = Punto(1.5, -2.6)
    
    # Triángulo 1
    triangulo1 = Poligono("Triángulo 1", [puntoA, puntoB, puntoC])
    
    # Triángulo 2 (comparte el lado A-B con el triángulo 1)
    triangulo2 = Poligono("Triángulo 2", [puntoA, puntoB, puntoD])
    
    print(triangulo1)
    print("\n" + str(triangulo2))
    print(f"\nLado común: {puntoA} - {puntoB}")
    print(f"El triángulo 1 y el triángulo 2 comparten los puntos: {puntoA} y {puntoB}")