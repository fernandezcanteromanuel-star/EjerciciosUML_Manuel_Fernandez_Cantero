from artista import Artista
from museo import Museo
from obra import Obra

if __name__ == '__main__':
    leonardo = Artista("Leonardo Da Vinci")
    anonimo = Artista("Anónimo")
    
    museo_prado = Museo("Museo del Prado", "Madrid")
    museo_louvre = Museo("Museo Louvre", "París")
    
    gioconda_original = Obra("La Gioconda", leonardo, 1503, 1516, "óleo sfumato", "madera de álamo", "Obra maestra original", museo_louvre)
    gioconda_replica = Obra("La Gioconda (Réplica)", anonimo, 1503, 1516, "óleo pincelada simple", "madera de nogal", "Réplica más antigua", museo_prado)
    
    print("=== OBRAS ===")
    print(gioconda_original)
    print(gioconda_replica)
    
    print(f"\n=== ARTISTAS Y SUS OBRAS ===")
    print(f"{leonardo.nombre} tiene {len(leonardo.obras)} obra(s)")
    print(f"{anonimo.nombre} tiene {len(anonimo.obras)} obra(s)")
    
    print(f"\n=== MUSEOS Y SUS OBRAS ===")
    print(f"{museo_louvre.nombre} tiene {len(museo_louvre.obras)} obra(s)")
    print(f"{museo_prado.nombre} tiene {len(museo_prado.obras)} obra(s)")