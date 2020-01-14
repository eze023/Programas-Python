class Productos():
	def getListaPeliculas(self):
		self.lista=["Avengers EndGame","Fury","Alien","Star Trek","The Notebook","Irene, Me and other Me"]
		return self.lista

	def getGenero(self):
		self.genero=["Accion","Belica","Terror","Ciencia Ficcion","Romantica","Comedia"]
		return self.genero

	def setTitulo(self, titulo):
		self.titulo=input("Ingrese el titulo de la pelicula: ")

	def getTitulo(self):
		return self.titulo

	def getListaAnio(self):
		self.listaAnio=["2019","2014","1979","2009","2004","2000"]
		return self.listaAnio

	def getListaDirector(self):
		self.listaDirector=["Antony Russo, Joe Russo","David Ayer","Ridley Scott","J.J. Abrams","Nick Cassavetes","Bobby Farrelly"]
		return self.listaDirector

	def getListaProtagonista(self):
		self.listaProtagonista=["Robert D. Jr, Chris Hemsworth, Chris Evans, Scarlett Johansson, Mark Ruffalo, Jeremy Renner, Tom Holland",
		"Brad Pitt, Logan Lerman, Shia LaBeouf, Jon Bernthal, Michael Peña",
		"Sigourney Weaver, John Hurt, Tom Skerritt","Chris Pine, Zachary Quinto, Zoe Saldaña, Leonard Nimoy","Ryan Gosling, Rachel McAdams",
		"Jim Carrey, Rene Zellweger"]
		return self.listaProtagonista

	def setPrecio(self, precio):
		self.precio=int(input("Ingrese el precio de alquiler: "))

	def getPrecio(self):
		return self.precio

	def setPlazo(self):
		self.plazo=int(input("Ingrese la cantidad de dias que desea alquilar: "))
		self.precio=self.precio*self.plazo
		return print("Los dias de alquiler son: "+str(self.plazo)+" el precio total sera: "+str(self.precio))

	def getPlazo(self):
		return self.plazo

	def getAlquiler(self, alquilar):
		self.listaAlquiler=[]
		self.alquilar=input("Ingrese el nombre de la pelicula a alquilar: ")
		if self.alquilar in self.lista and self.alquilar not in self.listaAlquiler:
			self.listaAlquiler.append(self.alquilar)
			print("Peliculas para alquilar: ",self.listaAlquiler)
		else:
			print("La pelicula no se encuentra para alquilar")

	def listarProductos(self):
		for i in range(len(self.lista)):
			print("Pelicula:",self.lista[i])
			print("Genero:",self.genero[i])
			print("Año:",self.listaAnio[i])
			print("Director:",self.listaDirector[i])
			print("Protagonistas",self.listaProtagonista[i])
			print()

	def agregaProductos(self):
		self.agregaPeli=input("Ingrese la pelicula a agregar: ")
		self.lista.append(self.agregaPeli)
		self.agregaGenero=input("Ingrese el genero de la pelicula: ")
		self.genero.append(self.agregaGenero)
		self.agregaAnio=input("Ingrese el año de la pelicula: ")
		self.listaAnio.append(self.agregaAnio)
		self.agregaDirector=input("Ingrese el director de la pelicula: ")
		self.listaDirector.append(self.agregaDirector)
		self.agregaProtagonista=input("Ingrese los protagonistas de la pelicula: ")
		self.listaProtagonista.append(self.agregaProtagonista)

class Cliente():
	def __init__(self, nombre, direccion, telefono):
		self.nombre=nombre
		self.direccion=direccion
		self.telefono=telefono

	def listaClientes(self):
		self.listaNombres=[]
		self.listaDireccion=[]
		self.listaTelefono=[]
		self.cantidad=int(input("Ingrese cuantos clientes desea cargar: "))
		for i in range(self.cantidad):
			self.nombre=input("Ingrese su nombre: ")
			self.listaNombres.append(self.nombre)
			self.direccion=input("Ingrese su direccion: ")
			self.listaDireccion.append(self.direccion)
			self.telefono=int(input("Ingrese su numero de telefono: "))
			self.listaTelefono.append(self.telefono)
			print()

	def listarCliente(self):
		for i in range(len(self.listaNombres)):
			print("Nombre:",self.listaNombres[i])
			print("Direccion:",self.listaDireccion[i])
			print("Telefono:",self.listaTelefono[i])
			print()

	def getNombre(self):
		return print("Nombre: ",self.nombre)

	def getDireccion(self):
		return print("Direccion: ",self.direccion)

	def getTelefono(self):
		return print("Numero de telefono: ",self.telefono)

	def alquilar(self):
		tipo=Productos()
		tipo.getListaPeliculas()
		tipo.getGenero()
		tipo.getListaAnio()
		tipo.getListaDirector()
		tipo.getListaProtagonista()

		self.respuesta=input("¿Desea agregar peliculas? si/no: ")
		self.respuesta.lower()
		while self.respuesta!="si" and self.respuesta!="no":
			print("Respuesta no valida")
			self.respuesta=input("¿Desea agregar peliculas? si/no: ")
			self.respuesta.lower()
		if self.respuesta=="si":
			tipo.agregaProductos()

		self.listado=input("¿Desea listar las peliculas en stock? si/no: ")
		self.listado.lower()
		while self.listado!="si" and self.listado!="no":
			self.listado=input("¿Desea listar las peliculas en stock? si/no: ")
			self.listado.lower()
		if self.listado=="si":
			tipo.listarProductos()
		else:
			print("Fin del programa...")

class Aplicacion():
	def __init__(self):
		tipo=Cliente("","","")
		tipo.listaClientes()
		tipo.listarCliente()
		tipo.alquilar()

tipo1=Aplicacion()