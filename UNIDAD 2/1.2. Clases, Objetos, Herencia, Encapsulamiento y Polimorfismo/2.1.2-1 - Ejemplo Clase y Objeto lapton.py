class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre} - Categoría: {self.categoria} - Precio: ${self.precio}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"El precio del producto {self.nombre} ha sido actualizado a ${self.precio}")


# Creación de Objetos:

producto1 = Producto("Laptop", "Electrónica", 1200)
producto1.mostrar_info()

producto2 = Producto("Libro", "Literatura", 20)
producto2.actualizar_precio(25)
producto2.mostrar_info()
