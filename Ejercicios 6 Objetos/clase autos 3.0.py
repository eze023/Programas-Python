class Auto():
    def salida(self):
        return print("Auto: "+self.marca+" Modelo: "+self.modelo)

class Marca(Auto):
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo


auto1=Marca("VW","Gol")
auto1.salida()

#creamos una clase auto con una funcion de salida la cual concatenara una herencia de la clase Marca cuya funcion esta inicializada para tomar los datos ingresados
#la salida sera la cadena de la funcion salida