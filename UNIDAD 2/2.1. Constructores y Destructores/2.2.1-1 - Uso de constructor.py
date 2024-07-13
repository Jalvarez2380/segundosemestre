# Ejemplo de Creación de Objetos:
# "Consideremos una clase Estudiante con un constructor definido.
# La creación de un objeto Estudiante se vería así en Python:"

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        """
        Constructor de la clase Estudiante.
        Inicializa los atributos nombre, edad y carrera del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

# Creación de una instancia de la clase Estudiante
mi_estudiante = Estudiante("Juan Pérez", 21, "Ingeniería de Sistemas")

# "Aquí, mi_estudiante es una instancia de la clase Estudiante, y se le pasan 'Juan Pérez',
# '21' y 'Ingeniería de Sistemas' como argumentos al constructor."
