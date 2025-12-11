class Libro:
    def __init__(self, id_libro, titulo, autor, tema):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.tema = tema
        self.disponible = True
    
    def __str__(self):
        return f"ID: {self.id_libro} | {self.titulo} por {self.autor} | Tema: {self.tema}"