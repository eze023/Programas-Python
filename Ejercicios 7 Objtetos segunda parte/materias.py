class Asignatura():
	def __init__(self, nombreAsignatura, notaAsignatura):
		self.nombreAsignatura=nombreAsignatura
		self.notaAsignatura=notaAsignatura

	def setNota(self):
		self.notaAsignatura=int(input("Ingrese la nota obtenida: "))
		while self.notaAsignatura>10 or self.notaAsignatura<1:
			print("Nota no valida, intente nuevamente")
			self.notaAsignatura=int(input("Ingrese la nota obtenida: "))
		return self.notaAsignatura

	def getNota(self, nota):
		self.notaAsignatura=nota
		if self.notaAsignatura>=1 and self.notaAsignatura<4:
			print("Desaprobado "+str(self.notaAsignatura))
		elif self.notaAsignatura>=4 and self.notaAsignatura<=10:
			print("Aprobado "+str(self.notaAsignatura))
		else:
			print("Nota no valida")

	def getAsignatura(self):
		self.notaAsignatura=input("Ingrese el nombre de la asignatura: ")
		return self.notaAsignatura

	def nameAsignatura(self):
		return self.nombreAsignatura

class Alumno():
	def __init__(self, nombreAlumno, edadAlumno):
		self.nombreAlumno=nombreAlumno
		self.edadAlumno=edadAlumno

	def setNombre(self):
		self.nombreAlumno=str(input("Ingrese su nombre: "))

	def getNombre(self):
		return print("Nombre: "+self.nombreAlumno)

	def setEdad(self):
		self.edadAlumno=int(input("Ingrese su edad: "))
		while self.edadAlumno<4 or self.edadAlumno>80:
			print("Edad no valida, intente nuevamente")
			self.edadAlumno=int(input("Ingrese su edad: "))
		return self.edadAlumno

	def getEdad(self):
		return print("Edad: "+str(self.edadAlumno))

	def promedio(self):
		self.listaNotas=[]
		suma=0
		tipo=Asignatura("",0)
		for i in range(3):
			self.listaNotas.append(tipo.setNota())
		for i in range(len(self.listaNotas)):
			suma+=self.listaNotas[i]
		b=len(self.listaNotas)
		prome=suma/b
		return tipo.getNota(prome)

	def agregaAsignatura(self):
		self.listaMaterias=[]
		tipo=Asignatura("",0)
		for i in range(3):
			if tipo.nameAsignatura() not in self.listaMaterias:
				self.listaMaterias.append(tipo.getAsignatura())
			else:
				print("La materia ya se encuentra en el plan de estudio!")
		return self.listaMaterias

	def salidaNotas(self):
		return self.listaNotas

	def salidaMaterias(self):
		return self.listaMaterias

class Aplicacion():
	def __init__(self):
		tipo1=Alumno(" ",0)
		tipo1.setNombre()
		tipo1.setEdad()
		tipo1.agregaAsignatura()
		tipo1.getNombre()
		tipo1.getEdad()
		for i in tipo1.salidaMaterias():
			print(i)
			tipo1.promedio()

chabon1=Aplicacion()
chabon2=Aplicacion()
chabon3=Aplicacion()

#el programa tiene 3 clases, en la clase alumno se toma los datos del alumno y llama a la clase asignatura para tomar los datos de las materias cursadas, luego realizara un promedio de las notas y a traves de la funcion promedio mostraremos en pantalla la salida
#la clase aplicacion es la que unifica todo el programa en si