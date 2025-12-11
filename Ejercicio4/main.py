from catedral import Catedral
from estilo import Estilo

if __name__ == '__main__':
    romanico = Estilo("Románico")
    gotico = Estilo("Gótico")
    barroco = Estilo("Barroco")
    plateresco = Estilo("Plateresco")
    neoclasico = Estilo("Neoclásico")
    
    catedral = Catedral("Catedral de Santiago de Compostela", "Santiago de Compostela", "La Coruña", "España", "Granito", 1075, 1122, 1211, 1896)
    
    catedral.agregar_estilo(romanico)
    catedral.agregar_estilo(gotico)
    catedral.agregar_estilo(barroco)
    catedral.agregar_estilo(plateresco)
    catedral.agregar_estilo(neoclasico)
    
    print(catedral)
    print(f"\nDéclarada Bien de Interés Cultural en {catedral.bien_interes_cultural}")