def modificar_linea_archivo(nombre_archivo, numero_linea, nuevo_contenido):
    """
    Modifica una línea específica en un archivo. Maneja excepciones para evitar errores durante la lectura o escritura.
    """
    try:
        # Leer el contenido original del archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

        # Verifica que la línea solicitada exista
        if 0 < numero_linea <= len(contenido):
            # Modificar la línea especificada
            contenido[numero_linea - 1] = nuevo_contenido + "\n"

            # Reescribir el archivo con la línea modificada
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(contenido)

            print(f"Línea {numero_linea} modificada correctamente.")
        else:
            print(f"El archivo '{nombre_archivo}' no tiene una línea {numero_linea}.")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except PermissionError:
        print(f"No se tienen permisos para modificar el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error inesperado al modificar el archivo: {e}")


# Ejemplo de uso
nombre_archivo = 'ejemplo.txt'

# Crear el archivo con contenido inicial
try:
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Línea 1\n")
        archivo.write("Línea 2\n")
        archivo.write("Línea 3\n")
    print(f"Archivo '{nombre_archivo}' creado con contenido inicial.")
except Exception as e:
    print(f"Error al crear el archivo: {e}")

# Leer y mostrar el contenido original
try:
    with open(nombre_archivo, 'r') as archivo:
        print(f"\nContenido Original de {nombre_archivo}:")
        print(archivo.read())
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")

# Modificar una línea específica y volver a imprimir
modificar_linea_archivo(nombre_archivo, 2, "Línea 2 modificada")

# Leer y mostrar el contenido modificado
try:
    with open(nombre_archivo, 'r') as archivo:
        print(f"\nContenido Modificado de {nombre_archivo}:")
        print(archivo.read())
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
