from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from elipse import Elipse

if __name__ == '__main__':
    circulo1 = Circulo("rojo", 10)
    rectangulo1 = Rectangulo(5, 8, "azul")
    cuadrado1 = Cuadrado(6, "verde")
    elipse1 = Elipse(12, 8, "amarillo")
    
    figuras = [circulo1, rectangulo1, cuadrado1, elipse1]
    
    print("=== FIGURAS GEOMÉTRICAS ===\n")
    for figura in figuras:
        print(figura)
        print(f"  Tipo: {type(figura).__name__}")
        print(f"  Color: {figura.color}\n")