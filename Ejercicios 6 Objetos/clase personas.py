class Persona():
	def __init__(self, nombre, edad, sexo):
		self.nombre=nombre
		self.edad=edad
		self.sexo=sexo

	def mayoromenor(self):
		if self.edad>=18:
			s="Mayor"
		elif self.edad<18:
			s="Menor"
		return s

	def sexos(self):
		if self.sexo=="m":
			s="Masculino"
		elif self.sexo=="f":
			s="Femenino"
		return s

	def salida(self):
		salida= "Nombre "+ self.nombre +" es "+ self.mayoromenor() + " y es de sexo " + self.sexos()
		return salida

a=Persona("Ezequiel", 29, "m")
b=Persona("Romina", 29, "f")
c=Persona("Ludmila", 7, "f")

print(a.salida())
print(b.salida())
print(c.salida())