class Lapton:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_identificacion(self):
        return f"Lapton de marca {self.marca}, modelo {self.modelo}"

class LaptonGamer(Lapton):
    def __init__(self, marca, modelo, tarjeta_grafica):
        super().__init__(marca, modelo)
        self.tarjeta_grafica = tarjeta_grafica

    def mostrar_detalles(self):
        informacion_base = super().mostrar_identificacion()
        return f"{informacion_base}, con tarjeta gráfica {self.tarjeta_grafica}"

# Creando un objeto de la clase Lapton
mi_lapton = Lapton("Dell", "Inspiron")
print(mi_lapton.mostrar_identificacion())

# Creando un objeto de la clase LaptonGamer
mi_lapton_gamer = LaptonGamer("MSI", "Predator", "NVIDIA RTX 3060")
print(mi_lapton_gamer.mostrar_detalles())

