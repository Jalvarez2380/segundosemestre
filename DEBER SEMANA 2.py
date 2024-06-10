class PersonajeNuevo:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class GuerreroNuevo(PersonajeNuevo):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hacha):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hacha = hacha

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Hacha de Guerra, daño 12. (2) Espada de Fuego, daño 15"))
        if opcion == 1:
            self.hacha = 12
        elif opcion == 2:
            self.hacha = 15
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Hacha:", self.hacha)

    def daño(self, enemigo):
        return self.fuerza * self.hacha - enemigo.defensa


class MagoNuevo(PersonajeNuevo):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, varita):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.varita = varita

    def atributos(self):
        super().atributos()
        print("·Varita:", self.varita)

    def daño(self, enemigo):
        return self.inteligencia * self.varita - enemigo.defensa


def combateNuevo(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1_nuevo = GuerreroNuevo("Aragorn", 18, 8, 6, 120, 5)
personaje_2_nuevo = MagoNuevo("Gandalf", 6, 16, 3, 100, 4)

personaje_1_nuevo.atributos()
personaje_2_nuevo.atributos()

combateNuevo(personaje_1_nuevo, personaje_2_nuevo)