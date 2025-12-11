from persona import Persona

if __name__ == '__main__':
    diana = Persona("Diana", "de Gales", "Spencer")
    carlos = Persona("Carlos", "de Gales", "Windsor")
    guillermo = Persona("Guillermo", "de Gales", "Windsor")
    kate = Persona("Kate", "Windsor", "Middleton")
    
    guillermo.set_padre(carlos)
    guillermo.set_madre(diana)
    guillermo.casarse(kate)
    
    print(f"{kate} y {guillermo} están casados")
    print(f"{guillermo} es hijo de {carlos} y {diana}")