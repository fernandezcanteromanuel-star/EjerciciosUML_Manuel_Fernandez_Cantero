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
    
    # Triángulo 2 (comparte los puntos A y B con el triángulo 1)
    triangulo2 = Poligono("Triángulo 2", [puntoA, puntoB, puntoD])
    
    print(triangulo1)
    print("\n" + str(triangulo2))
    
    print("\n=== ANÁLISIS DE PUNTOS COMPARTIDOS ===")
    print(f"Punto A {puntoA} pertenece a {len(puntoA.poligonos)} polígono(s):")
    for pol in puntoA.poligonos:
        print(f"  - {pol.nombre}")
    
    print(f"\nPunto B {puntoB} pertenece a {len(puntoB.poligonos)} polígono(s):")
    for pol in puntoB.poligonos:
        print(f"  - {pol.nombre}")
    
    print(f"\nPunto C {puntoC} pertenece a {len(puntoC.poligonos)} polígono(s):")
    for pol in puntoC.poligonos:
        print(f"  - {pol.nombre}")
    
    print(f"\nPunto D {puntoD} pertenece a {len(puntoD.poligonos)} polígono(s):")
    for pol in puntoD.poligonos:
        print(f"  - {pol.nombre}")