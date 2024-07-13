# "Consideremos una clase ConexionRed que simula la apertura y cierre
# de una conexión de red."

class ConexionRed:
    def __init__(self, id_conexion):
        self.id_conexion = id_conexion
        print(f"Conexión de red {self.id_conexion} establecida.")

    def __del__(self):
        print(f"Conexión de red {self.id_conexion} cerrada.")

# "Aquí, el destructor __del__ se encarga de liberar el recurso de la conexión de red.

# Al eliminar instancias de ConexionRed, se pueden observar las acciones del destructor:

mi_conexion = ConexionRed(1)
del mi_conexion

# La instancia mi_conexion de la clase ConexionRed es eliminada.
# Esto desencadena el destructor, gestionando adecuadamente el cierre de la conexión.
