class Auto():
    def salida(self):
        return print("Auto: "+self.marca+" Modelo: "+self.modelo)

class Marca(Auto):
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo


auto1=Marca("VW","Gol")
auto1.salida()