from libro import Libro
from muestra import Muestra

if __name__ == "__main__":
    # Ejemplo de Libro
    hojas = ["Página 1 manuscrita", "Página 2 impresa", "Página 3 impresa"]
    libro = Libro(hojas, encuadernado=True)
    libro.mostrar_info()
    print("¿Es volumen?", libro.es_volumen())

    # Ejemplo de Muestra
    conjunto = ["Elemento A", "Elemento B", "Elemento C", "Elemento D"]
    porcion = ["Elemento A", "Elemento C"]
    muestra = Muestra(porcion, conjunto, representativa=True)
    muestra.mostrar_info()
    print("¿Es válida?", muestra.es_valida())