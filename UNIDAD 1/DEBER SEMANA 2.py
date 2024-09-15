
class PersonajeNuevo:

    def __init__(self, nombre, poder_ataque, poder_magico, armadura, puntos_vida):
        self.nombre = nombre
        self.poder_ataque = poder_ataque
        self.poder_magico = poder_magico
        self.armadura = armadura
        self.puntos_vida = puntos_vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Poder de Ataque:", self.poder_ataque)
        print("·Poder Mágico:", self.poder_magico)
        print("·Armadura:", self.armadura)
        print("·Puntos de Vida:", self.puntos_vida)

    def subir_nivel(self, poder_ataque, poder_magico, armadura):
        self.poder_ataque += poder_ataque
        self.poder_magico += poder_magico
        self.armadura += armadura

    def esta_vivo(self):
        return self.puntos_vida > 0

    def morir(self):
        self.puntos_vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.poder_ataque - enemigo.armadura

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.puntos_vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.puntos_vida)
        else:
            enemigo.morir()


class GuerreroNuevo(PersonajeNuevo):

    def __init__(self, nombre, poder_ataque, poder_magico, armadura, puntos_vida, espada):
        super().__init__(nombre, poder_ataque, poder_magico, armadura, puntos_vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de Guerra, daño 12. (2) Hacha de Batalla, daño 15"))
        if opcion == 1:
            self.espada = 12
        elif opcion == 2:
            self.espada = 15
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.poder_ataque * self.espada - enemigo.armadura


class MagoNuevo(PersonajeNuevo):

    def __init__(self, nombre, poder_ataque, poder_magico, armadura, puntos_vida, varita):
        super().__init__(nombre, poder_ataque, poder_magico, armadura, puntos_vida)
        self.varita = varita

    def atributos(self):
        super().atributos()
        print("·Varita:", self.varita)

    def daño(self, enemigo):
        return self.poder_magico * self.varita - enemigo.armadura


def combateNuevo(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
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
