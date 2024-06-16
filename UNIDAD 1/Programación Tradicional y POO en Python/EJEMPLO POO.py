# Programación Orientada a Objetos (POO)
# Ejemplo: Calcular el promedio semanal del clima

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase Clima
clima = Clima()

# Uso de los métodos en la programación orientada a objetos
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    clima.ingresar_temperatura(temp)

promedio_semanal = clima.calcular_promedio()

# Imprimir el promedio semanal
print("El promedio semanal de las temperaturas (OOP) es:", promedio_semanal)
