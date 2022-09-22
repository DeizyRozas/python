class Mascota:
    def __init__( self, nombre, tipo , golosinas ):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud= 10
        self.energia= 5


    def dormir(self):
        self.energia +=25
        return self

    def comer(self):
        self.energia+= 5
        self.salud+= 10
        return self

    def jugar(self):
        self.salud += 5
        return self
        
    def ruido(self):
        print("miiau")

        return self

class Perro(Mascota):
    def __init__(self, nombre, tipo , golosinas):
        super().__init__(nombre, tipo , golosinas)

    def ruido(self):
        print("guauu")