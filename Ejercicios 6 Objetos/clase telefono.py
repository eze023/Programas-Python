class Telefono():
    def __init__(self, marca, modelo, costomensual):
        self.marca=marca
        self.modelo=modelo
        self.costomensual=costomensual

    def costoanual(self):
        self.costoanual=self.costomensual*12
        return self.costoanual

    def salida(self):
        return print("La marca es "+self.marca+" el modelo es "+self.modelo+" el costo anual es $ "+str(self.costoanual()))


telefono1=Telefono("Samsung","J8",900)
telefono1.salida()

#creamos una clase llamada telefono, con una funcion ya inicializada para luego tomar los datos del telefono en si y mostrar una cadena en pantalla con los datos ingresados