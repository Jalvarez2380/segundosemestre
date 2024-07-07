class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre} {self.apellido}, Salario: {self.salario}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario, departamento):
        super().__init__(nombre, apellido, salario)
        self.departamento = departamento

    def mostrar_detalle(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Departamento: {self.departamento}"

# Creando objetos de la clase Empleado y EmpleadoTiempoCompleto
empleado1 = Empleado("Juan", "Perez", 3000)
print(empleado1.mostrar_informacion())

empleado2 = EmpleadoTiempoCompleto("Maria", "Gomez", 4000, "Ventas")
print(empleado2.mostrar_detalle())
