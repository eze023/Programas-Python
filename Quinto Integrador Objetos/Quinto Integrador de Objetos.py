class Animal():
	def __init__(self):
		self.alimento=["omnivoro","carnivoro","herbivoro"]
	
	def getDietas(self):
		return self.alimento

class Puma(Animal):
	def __init__(self, id, peso):
		self.id=id
		self.peso=peso

	def pesos(self):
		if self.peso>=200:
			h="Sano"
		elif self.peso<200:
			h="Enfermo"
		return h

	def getId(self):
		return self.id

	def comida(self):
		self.dieta="carnivoro"
		comida=Animal()
		comida.getDietas()
		self.listaComida=[]
		self.listaComida=comida.getDietas()
		for i in range(len(self.listaComida)):
			if self.dieta in self.listaComida[i]:
				h=self.listaComida[i]
		return h

class Venado(Animal):
	def __init__(self, id, sexo, edad):
		self.id=id
		self.sexo=sexo
		self.edad=edad
		self.acumulador=0

	def edades(self):
		if self.edad>=5:
			self.acumulador=+1
		return self.acumulador

	def identi(self):
		return self.id

	def comida(self):
		self.dieta="herbivoro"
		comida=Animal()
		comida.getDietas()
		self.listaComida=[]
		self.listaComida=comida.getDietas()
		for i in range(len(self.listaComida)):
			if self.dieta in self.listaComida[i]:
				h=self.listaComida[i]
		return h

	def sexos(self):
		return self.sexo

class Jaula():
	def __init__(self):
		self.pumas=["Puma","Puma","Puma"]
		self.pesos=[230,178,212]
		self.venados=["Venado","Venado","Venado","Venado"]
		self.sexo=["Hembra","Macho","Hembra","Hembra"]
		self.edad=[2,6,5,3]
		self.jaulas=["Jaula 1","Jaula 2","Jaula 3"]

	def salida(self):
		acumulador=0
		x=0
		y=0
		for i in range(len(self.jaulas)):
			tipo=Puma(self.pumas[i],self.pesos[i])
			if i==0:
				print(self.jaulas[i], tipo.comida())
				for i in range(2):
					x+=1
					print(tipo.getId(),str(x), str(self.pesos[i])+"kg", tipo.pesos())
				print()

				tipo1=Venado(self.venados[i],self.sexo[i],self.edad[i])
				print(self.jaulas[i], tipo1.comida())
				for i in range(len(self.venados)):
					tipo1=Venado(self.venados[i],self.sexo[i],self.edad[i])
					y+=1
					print(tipo1.identi(),str(y), tipo1.sexos())
					acumulador+=tipo1.edades()
				print(str(acumulador)+" Adultos")
				print()

				for i in range(2,3):
					print(self.jaulas[i], tipo.comida())
					print(tipo.getId(),str(x), str(self.pesos[i])+"kg", tipo.pesos())
				print()

class Aplicacion():
	def __init__(self):
		self.tipo1=Jaula()
		self.tipo1.salida()


tipo=Aplicacion()