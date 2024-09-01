class Prestamo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = set()  # Conjunto para almacenar libros prestados únicos

    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.add(libro)
            print(f"Libro {libro} prestado con éxito en {self.nombre}.")
        else:
            print(f"Libro {libro} ya está prestado en {self.nombre}.")

# Ejemplo de uso
biblioteca_prestamos = Prestamo("Biblioteca Central")
biblioteca_prestamos.prestar_libro("978-3-16-148410-0")
biblioteca_prestamos.prestar_libro("978-0-395-19395-8")
biblioteca_prestamos.prestar_libro("978-3-16-148410-0")  # Intento de duplicar préstamo
