class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro
    
    def __str__(self):
        return f"Círculo - Color: {self.color}, Diámetro: {self.diametro}"