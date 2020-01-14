class Auto():
    def __init__(self, marca, anio):
        self.marca=marca
        self.anio=anio

    def antiguedad(self):
        self.total=2019-self.anio

    def salida(self):
        if self.total<5:
            pass
        else:
            print("La marca del auto es "+self.marca+" del año "+str(self.anio)+" su antiguedad es de "+str(self.total))
        

a1=Auto("Mercedes",1985)
a1.antiguedad()
a1.salida()

a2=Auto("Fiat",1990)
a2.antiguedad()
a2.salida()

a3=Auto("Ford",2015)
a3.antiguedad()
a3.salida()