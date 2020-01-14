class Motor():
	def arrancarMotor(self):
		print("Encendiendo el motor")

	
	def apagarMotor(self):
		print("Apagando el motor")
		
class Rueda():
	def __init__(self, uv, uh):
		self.uv=uv
		self.uh=uh

	def inflarRuedas(self):
		print("La rueda "+self.uv+" "+self.uh+" esta inflada")
	
	def desinflarRuedas(self):
		print("La rueda "+self.uv+" "+self.uh+" esta desinflada, se recomienda inflarla")

class Ventana():
	def __init__(self, uv):
		self.uv=uv

	def abrirVentana(self):
		print("Ventana "+self.uv+" abierta")

	def cerrarVentana(self):
		print("Ventana "+self.uv+" cerrada")

class Puerta():
	def __init__(self, uv):
		self.uv=uv

	def abrirPuerta(self):
		print("Abriendo puerta",self.uv)

	def cerrarPuerta(self):
		print("Cerrando la puerta", self.uv)

class Coche():
	def __init__(self):
		self.m=Motor()
		self.p1=Puerta("izquierda")
		self.p2=Puerta("derecha")
		self.v1=Ventana("izquierda")
		self.v2=Ventana("derecha")
		self.r1=Rueda("delantera", "izquierda")
		self.r2=Rueda("delantera", "derecha")
		self.r3=Rueda("trasera", "izquierda")
		self.r4=Rueda("trasera", "derecha")

a1=Coche()
a1.m.arrancarMotor()
a1.p1.abrirPuerta()
a1.v1.abrirVentana()
a1.p2.cerrarPuerta()
a1.v2.cerrarVentana()
a1.r1.inflarRuedas()
a1.r2.inflarRuedas()
a1.r3.desinflarRuedas()
a1.r4.inflarRuedas()
print("------------------")
a2=Coche()
a2.m.apagarMotor()
a2.v2.abrirVentana()
a2.v1.abrirVentana()
a2.r1.inflarRuedas()
a2.r2.inflarRuedas()
a2.r3.inflarRuedas()
a2.r4.inflarRuedas()
a2.p2.abrirPuerta()
a2.p1.abrirPuerta()
a2.p1.cerrarPuerta()
a2.p2.cerrarPuerta()