print("Ejercicio 7")

def cargadatos():
	nombres=[]
	sexo=[]
	for i in range(8):
		nombre=input("Ingrese su nombre: ")
		nombres+=[nombre]
		sexos=input("Ingrese su sexo m/f: ")
		sexo+=sexos

	return nombres, sexo

def nombresmujeres(lista1, lista2):
	nom=[]
	for i in range(len(lista2)):
		if lista2[i]=="f":
			nom+=[lista1[i]]

	return nom

nombres, sexos=cargadatos()
print()
print("Los nombres de las mujeres son: ", nombresmujeres(nombres, sexos))

#el programa a pesar de que este mismo se realizo en otra hoja de programacion
#utiliza funciones para implementar el uso de listas y determinar en una lista las mujeres que fueron ingresadas