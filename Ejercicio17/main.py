from tema import Tema
from libro import Libro
from lector import Lector
from empleado import Empleado
from estanteria import Estanteria
from planta import Planta
from prestamo import Prestamo

if __name__ == '__main__':
    # Crear temas
    infantil = Tema("Infantil")
    narrativa = Tema("Narrativa")
    ensayo = Tema("Ensayo")
    poesia = Tema("Poesía")
    
    # Crear libros
    libro1 = Libro("L001", "El Quijote", "Cervantes", narrativa)
    libro2 = Libro("L002", "Harry Potter", "Rowling", infantil)
    libro3 = Libro("L003", "Sapiens", "Harari", ensayo)
    
    # Crear plantas y estanterías
    planta1 = Planta(1)
    estanteria1 = Estanteria(1, 50)
    estanteria2 = Estanteria(2, 50)
    planta1.agregar_estanteria(estanteria1)
    planta1.agregar_estanteria(estanteria2)
    
    # Agregar libros a estanterías
    estanteria1.agregar_libro(libro1)
    estanteria1.agregar_libro(libro2)
    estanteria2.agregar_libro(libro3)
    
    # Crear lector y empleado
    lector1 = Lector("DNI001", "Juan García", "Calle Principal 123")
    empleado1 = Empleado("EMP001", "María López", "Calle Secundaria 456")
    
    # Crear préstamos
    prestamo1 = Prestamo(libro1, "10/12/2024", "25/12/2024", lector1)
    prestamo2 = Prestamo(libro2, "05/12/2024", "10/01/2025", empleado1)
    
    lector1.agregar_prestamo(prestamo1)
    empleado1.agregar_prestamo(prestamo2)
    
    print("=== INFORMACIÓN DE LA BIBLIOTECA ===\n")
    print(planta1)
    
    print("\n=== LIBROS EN LA BIBLIOTECA ===")
    print(libro1)
    print(libro2)
    print(libro3)
    
    print("\n=== USUARIO Y EMPLEADO ===")
    print(lector1)
    print(empleado1)
    
    print("\n=== PRÉSTAMOS ===")
    print(prestamo1)
    print(prestamo2)