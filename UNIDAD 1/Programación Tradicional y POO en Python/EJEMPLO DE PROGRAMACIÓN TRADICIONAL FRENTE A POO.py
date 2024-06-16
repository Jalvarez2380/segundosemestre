# Programación Tradicional
# Ejemplo: Calcular el promedio semanal del clima

# Definición de variables globales
temperaturas = []

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    global temperaturas
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio():
    global temperaturas
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones en la programación tradicional
ingresar_temperaturas()
promedio_semanal = calcular_promedio()

# Imprimir el promedio semanal
print(f"El promedio semanal de las temperaturas (Tradicional) es: {promedio_semanal:.2f}°C")


# Programación Orientada a Objetos (POO)
# Ejemplo: Calcular el promedio semanal del clima

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase Clima
clima = Clima()

# Uso de los métodos de la clase
clima.ingresar_temperaturas()
promedio_semanal = clima.calcular_promedio()

# Imprimir el promedio semanal
print(f"El promedio semanal de las temperaturas (OOP) es: {promedio_semanal:.2f}°C")
