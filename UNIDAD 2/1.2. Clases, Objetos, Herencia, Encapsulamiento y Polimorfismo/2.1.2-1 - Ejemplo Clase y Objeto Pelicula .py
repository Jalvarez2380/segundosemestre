class Pelicula:
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion

    def informacion(self):
        return f"{self.titulo}, dirigida por {self.director}, duración: {self.duracion} minutos"


# Instanciación
mi_pelicula = Pelicula("El Padrino", "Francis Ford Coppola", 175)
print(mi_pelicula.informacion())

