class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.datos = (titulo, autor)  # Tupla para datos inmutables como título y autor
        self.categoria = categoria

    def __str__(self):
        titulo, autor = self.datos
        return f"{titulo} por {autor}, ISBN: {self.isbn}, Categoría: {self.categoria}"

class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista para manejar libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print("No hay libros prestados.")
        else:
            print("Libros prestados a este usuario:")
            for libro in self.libros_prestados:
                print(libro)

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para manejar IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario.usuario_id)

    def dar_baja_usuario(self, usuario_id):
        self.usuarios.remove(usuario_id)

    def buscar_libro(self, criterio, valor):
        for libro in self.libros.values():
            if getattr(libro, criterio) == valor:
                print(libro)

# Ejemplo de uso
biblioteca = Biblioteca()
libro1 = Libro("978-3-16-148410-0", "El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía")
biblioteca.agregar_libro(libro1)
usuario1 = Usuario("Juan Pérez", "001")
biblioteca.registrar_usuario(usuario1)

usuario1.prestar_libro(libro1)
usuario1.mostrar_libros_prestados()

biblioteca.buscar_libro("categoria", "Fantasía")
