class BotonPanico:
    def presionar(self, nivel='bajo'):
        if nivel == 'bajo':
            return "Se ha presionado el botón de pánico a un nivel bajo"
        elif nivel == 'medio':
            return "Se ha presionado el botón de pánico a un nivel medio"
        elif nivel == 'alto':
            return "Se ha presionado el botón de pánico a un nivel alto"
        else:
            return "Nivel no reconocido al presionar el botón de pánico"

# Creando un objeto de la clase BotonPanico
mi_boton_panico = BotonPanico()

# Simulando la presión del botón con diferentes niveles
print(mi_boton_panico.presionar())  # Nivel bajo (por defecto)
print(mi_boton_panico.presionar('medio'))  # Nivel medio
print(mi_boton_panico.presionar('alto'))  # Nivel alto
print(mi_boton_panico.presionar('máximo'))  # Nivel no reconocido
