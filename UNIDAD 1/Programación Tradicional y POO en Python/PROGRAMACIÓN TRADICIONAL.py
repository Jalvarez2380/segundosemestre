# Programación Tradicional
# Ejemplo: Calcular el promedio semanal del clima

# Definición de variables globales
temperaturas = []

# Función para ingresar temperaturas diarias
def ingresar_temperatura(temp):
    global temperaturas
    temperaturas.append(temp)

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio():
    global temperaturas
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones en la programación tradicional
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    ingresar_temperatura(temp)

promedio_semanal = calcular_promedio()

# Imprimir el promedio semanal
print("El promedio semanal de las temperaturas (Tradicional) es:", promedio_semanal)
