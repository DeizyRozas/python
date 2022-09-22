from mascotas import Mascota

class Ninja():
    def __init__(self, nombre, mascota, premios, comida_mascota):
        self.nombre = nombre
        self.mascota = mascota
        self.premio = premios
        self.comida_mascota = comida_mascota

    def alimentar(self):
        self.mascota.comer()
        print("la energia de",self.mascota.nombre,"ha aumentado a:", self.mascota.energia, "y la salud a:", self.mascota.salud)
        return self

    def caminar(self):
        self.mascota.jugar()
        print(self.mascota.nombre, "ha paseado y su salud aumenta a:", self.mascota.salud)
        return self

    def bañar(self):
        self.mascota.ruido()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
