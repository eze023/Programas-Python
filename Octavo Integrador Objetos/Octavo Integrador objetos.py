class Liquid():
	def setName(self, name):
		self.name=name

	def setType(self, types):
		self.types=types

	def setSubType(self, subType):
		self.subType=subType

	def setNicotine(self, nicotine):
		self.nicotine=nicotine

	def getName(self):
		return self.name

	def getType(self):
		return self.types

	def getSubType(self):
		return self.subType

	def getNicotine(self):
		return self.nicotine

	def salida(self):
		if self.types=="tabaquil":
			return self.name +" "+self.types +" "+ self.subType +" "+ str(self.nicotine)+"%"
		elif self.types=="frutal":
			return self.name +" "+ self.types +" "+ str(self.nicotine)+"%"
		

class Tabaquil(Liquid):
	def __init__(self, name, types):
		self.name=name
		self.types=types
		if self.types=="tabaquil" and self.name=="Amsterdam":
			print("Vapor Amsterdam")
			self.subType=input("Rubio o Negro?: ")
			self.nicotine=3
		elif self.types=="tabaquil" and self.name=="Tribeca":
			print("Vapor Tribeca")
			self.subType=input("¿Rubio, Negro o Mentolado?: ")
			self.nicotine=3


class Frutal(Liquid):
	def __init__(self, name, types):
		self.name=name
		self.types=types
		if self.types=="frutal":
			print("Vapor Frutal")
			self.nicotine=input("¿Cuanta cantidad de nicotina? 0, 3 o 6: ")


class Stock():
	def __init__(self):
		self.stockInicial=[["Amsterdam", "tabaquil", 2], ["Naranja", "frutal", 3], ["Tribeca", "tabaquil", 2]]

	def altaStock(self):
		lista=[]
		self.name=input("Ingrese el nombre del vapor: ")
		self.types=input("Ingrese el tipo de vapor: ")
		self.cantidad=1
		lista.append(self.name)
		lista.append(self.types)
		lista.append(self.cantidad)
		self.stockInicial.append(lista)

	def outSide(self):
		lista=[]
		for i in range(len(self.stockInicial)):
			a, b, c=self.stockInicial[i]
			for i in range(c):
				if b=="tabaquil":
					vapor=Tabaquil(a, b)
					lista.append(vapor.salida())
				elif b=="frutal":
					vapor1=Frutal(a, b)
					lista.append(vapor1.salida())
		print()
		for i in range(len(lista)):
			print(lista[i])
		print()
			
cosa=Stock()
cosa.altaStock()
cosa.altaStock()
cosa.outSide()