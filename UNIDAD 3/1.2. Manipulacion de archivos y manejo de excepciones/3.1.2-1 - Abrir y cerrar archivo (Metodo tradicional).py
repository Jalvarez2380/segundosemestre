# Abre el archivo en modo lectura y maneja excepciones.
try:
    with open('ejemplo_lectura.txt', 'r') as archivo:
        print(archivo.read())  # Imprime el contenido del archivo
except FileNotFoundError:
    print("El archivo 'ejemplo_lectura.txt' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

# Abre el archivo en modo escritura (creándolo si no existe) y maneja excepciones.
try:
    with open('ejemplo_escritura.txt', 'w') as archivo:
        archivo.write('Este es un nuevo archivo.')  # Escribe en el archivo
except PermissionError:
    print("No se tienen permisos para escribir en 'ejemplo_escritura.txt'.")
except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Abre el archivo en modo añadir, añade una nueva línea y maneja excepciones.
try:
    with open('ejemplo_escritura.txt', 'a') as archivo:
        archivo.write('\nAñadiendo una segunda línea.')  # Añade nueva línea de texto al archivo
except PermissionError:
    print("No se tienen permisos para escribir en 'ejemplo_escritura.txt'.")
except Exception as e:
    print(f"Ocurrió un error al añadir contenido en el archivo: {e}")

# Abre el archivo en modo lectura y maneja excepciones.
try:
    with open('ejemplo_escritura.txt', 'r') as archivo:
        print(archivo.read())  # Imprime el contenido del archivo
except FileNotFoundError:
    print("El archivo 'ejemplo_escritura.txt' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
