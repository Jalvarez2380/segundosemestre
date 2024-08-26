class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo. Si el archivo no existe, lo crea vacío.
        Maneja excepciones en caso de errores durante la lectura.
        """
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, cantidad = linea.strip().split(',')
                    self.productos[nombre] = int(cantidad)
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará un nuevo archivo.")
            open(self.archivo, 'w').close()  # Crear un archivo vacío
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda el inventario actual en el archivo.
        Maneja excepciones durante la escritura para asegurar que el archivo se guarde correctamente.
        """
        try:
            with open(self.archivo, 'w') as f:
                for nombre, cantidad in self.productos.items():
                    f.write(f"{nombre},{cantidad}\n")
            print("Inventario guardado correctamente.")
        except PermissionError:
            print(f"No se tienen permisos para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """
        Añade un producto al inventario o actualiza la cantidad si ya existe.
        Luego guarda los cambios en el archivo.
        """
        if nombre in self.productos:
            self.productos[nombre] += cantidad
            print(f"Producto '{nombre}' actualizado. Nueva cantidad: {self.productos[nombre]}.")
        else:
            self.productos[nombre] = cantidad
            print(f"Producto '{nombre}' añadido al inventario con cantidad: {cantidad}.")
        self.guardar_inventario()

    def actualizar_producto(self, nombre, cantidad):
        """
        Actualiza la cantidad de un producto existente en el inventario.
        Si el producto no existe, se notifica al usuario.
        """
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print(f"Producto '{nombre}' actualizado a cantidad: {cantidad}.")
            self.guardar_inventario()
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario si existe.
        Si el producto no existe, se notifica al usuario.
        """
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
            self.guardar_inventario()
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

# Ejemplo de uso
inventario = Inventario()
inventario.agregar_producto('Manzanas', 50)
inventario.agregar_producto('Naranjas', 30)
inventario.actualizar_producto('Manzanas', 75)
inventario.eliminar_producto('Naranjas')
