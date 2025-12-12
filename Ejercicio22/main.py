from ciudad import Ciudad
from espacio import Calle, Plaza
from edificio import Edificio
from fachada import Fachada
from elementos import Portada, Puerta, Ventana, Balcon

if __name__ == "__main__":
    # Crear ciudad
    ciudad = Ciudad("Madrid")

    # Crear espacios
    calle = Calle("Gran Vía", 1300)
    plaza = Plaza("Plaza Mayor", 5000)

    # Crear edificios
    edificio1 = Edificio("Edificio Telefónica", 14)
    edificio2 = Edificio("Casa de la Panadería", 4)

    # Crear fachadas
    fachada1 = Fachada("Barroco")
    fachada1.agregar_elemento(Portada("piedra", "esculturas"))
    fachada1.agregar_elemento(Puerta("madera", "doble hoja"))
    fachada1.agregar_elemento(Ventana("vidrio", "rectangular"))

    fachada2 = Fachada("Renacentista")
    fachada2.agregar_elemento(Balcon("hierro", 3))
    fachada2.agregar_elemento(Ventana("vidrio", "arco"))

    # Asociar fachadas a edificios
    edificio1.agregar_fachada(fachada1)
    edificio2.agregar_fachada(fachada2)

    # Asociar edificios a espacios
    calle.agregar_edificio(edificio1)
    plaza.agregar_edificio(edificio2)

    # Asociar espacios a ciudad
    ciudad.agregar_espacio(calle)
    ciudad.agregar_espacio(plaza)

    # Mostrar información completa
    ciudad.mostrar_info()
