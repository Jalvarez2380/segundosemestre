try:
    # Intenta ejecutar este bloque de código que puede lanzar excepciones
    resultado = 10 / 0  # Esto provocará un ZeroDivisionError
    #resultado = int("no es un número")  # Descomenta para probar ValueError
except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Por favor, verifica tus operaciones matemáticas.")
except ValueError:
    print("Error: El valor proporcionado no es un número válido. Asegúrate de ingresar datos correctos.")
except Exception as e:
    # Captura cualquier otra excepción no capturada por los except anteriores
    print(f"Error inesperado: {e}")
finally:
    # Este bloque se ejecuta siempre, ocurra o no una excepción
    print("La ejecución del bloque try-except ha finalizado.")
