
class Cuenta():
	def __init__(self, numC, dni, saldo, interes):
		self.numC=numC
		self.dni=dni
		self.saldo=saldo
		self.interes=interes

	def ingresar(self, ingreso):
		self.ingreso=ingreso
		self.saldo=self.saldo+self.ingreso

	def intereses(self):
		self.interes=((self.saldo*self.interes)/100)/365
		self.saldo=self.saldo+self.interes

	def retiro(self, retiro):
		self.retiro=retiro
		if self.retiro>self.saldo:
			print("No se puede retirar mas dinero del que se encuentra en la cuenta")
			print("Su saldo actual es de :",self.saldo)
		else:
			self.saldo=self.saldo-self.retiro

	def salida(self):
		print("Estado de cuenta "+self.numC+" numero de DNI "+self.dni+" saldo actual "+str(self.saldo))

tipo1=Cuenta("10001","35.134.023",50000,10)
tipo1.ingresar(10000)
tipo1.intereses()
tipo1.retiro(150)
tipo1.salida()
print("-------------------")
tipo2=Cuenta("10002","34.885.941",20000,25)
tipo2.ingresar(2000)
tipo2.intereses()
tipo2.retiro(1000)
tipo2.salida()
print("-------------------")
tipo3=Cuenta("10003", "16.859.944",15000,5)
tipo3.ingresar(0)
tipo3.intereses()
tipo3.retiro(20000)
tipo3.salida()