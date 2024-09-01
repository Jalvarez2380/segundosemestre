class Usuario:
    def __init__(self, usuario_id, nombre):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.libros_prestados = []  # Lista para manejar los libros prestados

    def __str__(self):
        return f"ID: {self.usuario_id}, Nombre: {self.nombre}, Libros Prestados: {[libro.datos[0] for libro in self.libros_prestados]}"

class GestionUsuarios:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar objetos Usuario
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        # La clave es el ID del usuario, facilitando una búsqueda rápida
        self.usuarios[usuario.usuario_id] = usuario

    def dar_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            del self.usuarios[usuario_id]
            print(f"Usuario {usuario_id} dado de baja con éxito.")
        else:
            print("Usuario no encontrado.")

    def buscar_usuario(self, usuario_id):
        # Acceso directo al usuario mediante su ID
        return self.usuarios.get(usuario_id, "Usuario no encontrado.")

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            print(usuario)

# Ejemplo de uso
gestion = GestionUsuarios()
gestion.registrar_usuario(Usuario("001", "Juan Pérez"))
gestion.registrar_usuario(Usuario("002", "Ana Gómez"))

print("Búsqueda de usuario por ID:")
print(gestion.buscar_usuario("001"))
print(gestion.buscar_usuario("003"))  # ID inexistente

print("\nListado completo de usuarios:")
gestion.mostrar_usuarios()

# Dar de baja a un usuario y mostrar el listado actualizado
gestion.dar_baja_usuario("001")
print("\nListado después de dar de baja a un usuario:")
gestion.mostrar_usuarios()
