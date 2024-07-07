class Laptop:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class GamingLaptop(Laptop):  # Herencia de la clase Laptop
    def __init__(self, marca, modelo, tarjeta_grafica):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase padre
        self.tarjeta_grafica = tarjeta_grafica

    # Método específico de la clase GamingLaptop
    def mostrar_informacion(self):
        return f"Laptop Gaming {self.marca} {self.modelo}, con tarjeta gráfica {self.tarjeta_grafica}"

class Ultrabook(Laptop):
    def __init__(self, marca, modelo, peso):
        super().__init__(marca, modelo)
        self.peso = peso

    def mostrar_informacion(self):
        return f"Ultrabook {self.marca} {self.modelo}, peso {self.peso} kg"

# Creación de un objeto de la clase GamingLaptop
mi_gaming_laptop = GamingLaptop("MSI", "Predator", "NVIDIA RTX 3080")
print(mi_gaming_laptop.mostrar_informacion())

# Creación de un objeto de la clase Ultrabook
mi_ultrabook = Ultrabook("Dell", "XPS 13", 1.2)
print(mi_ultrabook.mostrar_informacion())
