# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    return lado * lado

# Ingreso de los lados del cuadrado por el usuario
lado_cuadrado = input("Ingresa la longitud de un lado del cuadrado: ")

# Verificación de que el valor ingresado sea numérico
if lado_cuadrado.replace('.', '', 1).isdigit():
    lado_cuadrado = float(lado_cuadrado)
    area_cuadrado = calcular_area_cuadrado(lado_cuadrado)
    if isinstance(area_cuadrado, int):
        print(f"El área del cuadrado con lado {lado_cuadrado} es: {int(area_cuadrado)}")
    else:
        print(f"El área del cuadrado con lado {lado_cuadrado} es: {area_cuadrado}")
else:
    print("Por favor, ingresa un valor numérico para el lado del cuadrado.")
