class Cafetera():
	def __init__(self, capacidadM, capacidadA):
		self.capacidadM=capacidadM
		self.capacidadA=capacidadA

	def llenarCafetera(self, cantidad):
		self.cantidad=cantidad
		self.capacidadA+=self.cantidad
		if self.capacidadA<=self.capacidadM:
			self.capacidadA=self.cantidad
		elif self.capacidadA>self.capacidadM:
			print("No puede llenar la cafetera mas del limite ")
			self.cantidad=1000
			self.capacidadA=1000

	def servirCafe(self, taza):
		self.taza=taza
		if self.capacidadA<self.taza:
			self.taza=self.capacidadA
			self.capacidadA=0
			self.queda=self.capacidadA
		elif self.capacidadA>=self.taza:
			self.capacidadA-=self.taza
			self.queda=self.capacidadA

	def salida(self):
		print("En la cafetera habia: "+str(self.cantidad)+"c.c., servi una taza de cafe quedo "+str(self.capacidadA)+"c.c.")

tipo1=Cafetera(1000,0)
tipo1.llenarCafetera(900)
tipo1.servirCafe(250)
tipo1.salida()
print("--------------")
tipo2=Cafetera(1000,100)
tipo2.llenarCafetera(1000)
tipo2.servirCafe(250)
tipo2.salida()
print("--------------")
tipo3=Cafetera(1000,0)
tipo3.llenarCafetera(200)
tipo3.servirCafe(250)
tipo3.salida()

#este programa realiza la funcion de una cafetera, al momento de estar vacia avisara que no quedo cafe dentro de la misma, en caso de que estuviera llena avisara que no se puede cargar mas
#en caso de estar media vacia procedera a llenar cierta cantidad de liquido