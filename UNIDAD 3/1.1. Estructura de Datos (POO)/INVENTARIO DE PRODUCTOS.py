# Definición de la clase Producto con atributos y métodos usando property
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Propiedad para ID
    @property
    def id(self):
        return self._id

    # Propiedad para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Propiedad para cantidad
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    # Propiedad para precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Método especial para convertir el objeto en una cadena de texto
    def __str__(self):
        return f"{self.id} {self.nombre} {self.cantidad} {self.precio}"

# Definición de la clase Inventario para manejar una lista de productos
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verifica que el ID sea único
        for p in self.productos:
            if p.id == producto.id:
                print(f"Error: Ya existe un producto con el ID {producto.id}.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                print(f"Producto con ID {id} eliminado exitosamente.")
                return
        print(f"Error: No se encontró un producto con el ID {id}.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                print(f"Producto con ID {id} actualizado exitosamente.")
                return
        print(f"Error: No se encontró un producto con el ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for p in self.productos:
                print(p)

# Interfaz de usuario en consola
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione enter para dejarla igual): ")
            precio = input("Ingrese el nuevo precio (o presione enter para dejarlo igual): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecuta el menú
if __name__ == "__main__":
    menu()
