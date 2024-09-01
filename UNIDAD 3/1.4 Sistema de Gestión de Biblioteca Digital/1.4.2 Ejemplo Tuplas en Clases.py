class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        # Los datos de título y autor son inmutables y se guardan en una tupla
        self.datos = (titulo, autor)
        self.categoria = categoria

    def __str__(self):
        # Convertir la tupla datos a una representación en string
        titulo, autor = self.datos
        return f"ISBN: {self.isbn} - '{titulo}' por {autor}, Categoría: {self.categoria}"

# Ejemplo de uso
libro1 = Libro("978-3-16-148410-0", "El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía")
print(libro1)

# Intento de modificar el título o el autor directamente resultará en un error
# libro1.datos[0] = "El Hobbit"  # Esto causaría un TypeError debido a que las tuplas son inmutables
