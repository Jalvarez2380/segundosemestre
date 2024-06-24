class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"{self.titulo} - {self.autor} - ${self.precio}"

class TiendaLibros:
    def __init__(self):
        self.inventario = []

    def agregar_libro(self, libro):
        self.inventario.append(libro)
        print(f"Libro '{libro.titulo}' agregado al inventario.")

    def mostrar_inventario(self):
        print("Inventario de la tienda:")
        for libro in self.inventario:
            print(libro)

# Crear algunos libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 15)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 20)
libro3 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 18)

# Crear la tienda de libros
tienda = TiendaLibros()

# Agregar libros al inventario
tienda.agregar_libro(libro1)
tienda.agregar_libro(libro2)
tienda.agregar_libro(libro3)

# Mostrar el inventario
tienda.mostrar_inventario()