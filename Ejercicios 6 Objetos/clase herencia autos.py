class Auto():
    def __init__(self, marca, anio):
        self.marca=marca
        self.anio=anio

    def salida(self):
    	if self.color:
    		var=print("La marca del auto es "+self.marca+" del año "+str(self.anio)+" su dueño es "+self.dueño+" y es de color "+self.color)

    	return var


class Tuauto(Auto):
		def dueñoColor(self, dueño, color):
			self.dueño=dueño
			self.color=color


color=input("Ingrese el color del auto que le interesa encontrar: ")

if color in ("rojo"):
	a1=Tuauto("Mercedes",1985)
	a1.dueñoColor("Marcos","rojo")
	a1.salida()

	a2=Tuauto("Volkswagen",1945)
	a2.dueñoColor("Jose", "rojo")
	a2.salida()
elif color in ("gris","plateado"):
	a3=Tuauto("Ferrari",2015)
	a3.dueñoColor("Pedro","gris")
	a3.salida()

	a4=Tuauto("Ford",2018)
	a4.dueñoColor("Juan","plateado")
	a4.salida()
else:
	print("No existen autos con ese color")

#creamos dos clases una que determina los datos del auto, y otra que asigna al dueño los datos del auto