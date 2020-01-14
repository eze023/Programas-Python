class Auto():
    def __init__(self, marca, anio):
        self.marca=marca
        self.anio=anio

    def salida(self):
        return print("La marca del auto es "+self.marca+" del año "+str(self.anio))

a1=Auto("Mercedes",1985)
a1.salida()

a2=Auto("Fiat",1990)
a2.salida()

a3=Auto("Ford",2015)
a3.salida()