class Telefono():
	def __init__(self, marca, modelo, so, version, costo, memoria):
		self.marca=marca
		self.modelo=modelo
		self.so=so
		self.version=version
		self.costo=costo
		self.memoria=memoria

	def costo1(self):
		return self.costo*12

	def memoria1(self):
		if self.memoria>6:
			aux="alta gama"
		else:
			aux="baja gama"

		return aux

	def salida(self):
		return print("El costo anual del telefono es $"+str(self.costo1())+" su version de sistema operativo es "+self.so,self.version+" y es un telefono de "+self.memoria1())


cel1=Telefono("Samsung","J8","Android","6.0",900,4)
cel1.salida()

cel2=Telefono("Iphone","X","iOS","10",3000,16)
cel2.salida()