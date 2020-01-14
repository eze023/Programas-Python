class Employ():
	def setName(self, name):
		self.name=name

	def getName(self):
		return self.name

	def setPay(self, pay):
		self.pay=pay

	def getPay(self):
		return self.pay


class Programmer(Employ):
	def __init__(self, progLang):
		self.progLang=progLang

	def setProyect(self, proyect):
		self.proyect=proyect

	def setSituation(self, situation):
		self.situation=situation

	def salida(self):
		return "Lenguaje: "+self.progLang+", Proyecto: "+ self.proyect+", Situacion: "+self.situation+", Salario: $"+str(self.pay)


class Company():
	def __init__(self):
		self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
		self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML&CSS"]
		self.listaProgramadores = []
		self.name=input("Ingrese su nombre: ")
		self.job=input("Ingrese el rubro: ")

	def getJob(self):
		return self.name, self.job

	def agEmp(self):
		if self.job=="Programador":
			self.progLang=input("¿Que lenguaje de programacion utiliza?: ")
			tipo=Programmer(self.progLang)
			tipo.setName(self.name)
			tipo.setSituation("sin comenzar")
			if self.progLang in self.listaLenguajes:
				if self.progLang=="Python":
					tipo.setPay(25000)
					self.listaProgramadores.append(tipo.getName())
					print(self.listaProyectos)
					proyect=int(input("Elija un proyecto 1 - 2: "))
					if proyect==1:
						proyect=self.listaProyectos[0]
						tipo.setProyect(proyect)
					elif proyect==2:
						proyect=self.listaProyectos[1]
						tipo.setProyect(proyect)
				elif self.progLang!="Python":
					tipo.setPay(17000)
					self.listaProgramadores.append(tipo.getName())
					print(self.listaProyectos)
					proyect=int(input("Elija un proyecto 1 - 2: "))
					if proyect==1:
						proyect=self.listaProyectos[0]
						tipo.setProyect(proyect)
					elif proyect==2:
						proyect=self.listaProyectos[1]
						tipo.setProyect(proyect)
			elif self.progLang not in self.listaLenguajes:
				tipo.setPay(0)
				proyect=" "
				tipo.setProyect(proyect)
			self.salida=tipo.salida()
		else:
			print("Solo se necesitan Programadores")

	def showAll(self):
		if self.job=="Programador" and self.progLang in self.listaLenguajes:
			for i in range(len(self.listaProgramadores)):
				print("Empresa Red Baron, "+self.job+": "+self.listaProgramadores[i]+", "+self.salida)
		elif self.job=="Programador" and self.progLang not in self.listaLenguajes:
			print("No se necesita ese lenguaje de programacion")
			print(self.listaLenguajes)

for i in range(3):
	tipo=Company()
	tipo.agEmp()
	tipo.showAll()