class Listas():
	def tomadedatos(self):
		self.num=int(input("Ingrese la cantidad de nombres a cargar: "))

	def operacion(self):
		self.lista=[]
		for i in range(self.num):
			self.nombre=str(input("Ingrese su nombre: "))
			self.lista+=[self.nombre]
		return self.lista

	def salida(self):
		print(self.lista)


num=Listas()
num.tomadedatos()
num.operacion()
num.salida()