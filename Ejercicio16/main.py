from persona import Persona

if __name__ == '__main__':
    diana = Persona("Diana", "de Gales", "Spencer", "01/07/1961", "Mujer", "DG001")
    carlos = Persona("Carlos", "de Gales", "Windsor", "14/11/1948", "Hombre", "CW001")
    guillermo = Persona("Guillermo", "de Gales", "Windsor", "21/06/1982", "Hombre", "GW001")
    kate = Persona("Kate", "Windsor", "Middleton", "09/01/1982", "Mujer", "KW001")
    
    # Relaciones familiares
    guillermo.set_padre(carlos)
    guillermo.set_madre(diana)
    guillermo.casarse(kate)
    
    print("=== PERSONAS ===\n")
    print(guillermo)
    print("\n" + "="*50 + "\n")
    print(kate)
    print("\n" + "="*50 + "\n")
    print(carlos)
    print("\n" + "="*50 + "\n")
    print(diana)
    
    print("\n" + "="*50)
    print("=== RESUMEN DE RELACIONES FAMILIARES ===\n")
    print(f"{kate.nombre} y {guillermo.nombre} están casados")
    print(f"{guillermo.nombre} es hijo de {carlos.nombre} y {diana.nombre}")