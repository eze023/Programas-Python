class Cancion():
	def __init__(self, titulo, autor):
		self.titulo=titulo
		self.autor=autor

	def dameTitulo(self):
		print("El titulo de la cancion es: "+self.titulo)

	def dameAutor(self):
		print("El autor de la cancion es: "+self.autor)

	def ponerTitulo(self, cancion):
		self.titulo=cancion

	def ponerAutor(self, cantante):
		self.autor=cantante

tema=Cancion("","")
tema.ponerTitulo("Seven pillars of wisdom")
tema.ponerAutor("Sabaton")
tema.dameTitulo()
tema.dameAutor()

#este programa cumple la funcion de composicion muestra en pantalla el titulo de la cancion ingresada y el autor