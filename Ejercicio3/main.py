from artista import Artista
from museo import Museo
from obra import Obra

if __name__ == '__main__':
    leonardo = Artista("Leonardo Da Vinci")
    anonimo = Artista("Anónimo")
    
    museo_prado = Museo("Museo del Prado", "Madrid")
    museo_louvre = Museo("Museo Louvre", "París")
    
    gioconda_original = Obra("La Gioconda", leonardo, 1503, 1516, "óleo sfumato", "madera de álamo", "Obra maestra original", museo_louvre)
    gioconda_replica = Obra("La Gioconda (Réplica)", anonimo, 1503, 1516, "óleo pincelada simple", "madera de nogal", "Réplica más antigua conocida", museo_prado)
    
    print(gioconda_original)
    print(gioconda_replica)
    print(f"\n{gioconda_original.titulo} está en {gioconda_original.museo}")
    print(f"{gioconda_replica.titulo} está en {gioconda_replica.museo}")