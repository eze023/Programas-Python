print("Ejercicio 8")

def cargadedatos():
	lista=[]
	car="si"
	while car!="no":
		datos=input("Ingrese un nombre: ")
		lista+=[datos]
		carga=input("Desea seguir cargando datos? si/no: ")
		car=carga.lower()

	return lista

def buscar(lista):
	indice=0
	car="si"
	if car!="no":
		car=input("Desea buscar un nombre? si/no: ")
		car=car.lower()
		if car!="no":
			nombre=input("Ingrese el nombre que desea buscar: ")
			for i in range(len(lista)):
				if lista[i]==nombre:
					indice=i
		else:
			indice=print("No se realizo ninguna busqueda")

	return indice

print()
nombres=cargadedatos()
print()
print("El lugar de la lista del nombre buscado es: ", buscar(nombres))

#el programa pide el ingreso de un nombre para ir agregando a la lista, una vez finalizada la carga de nombres pregunta si desea buscar alguno de los ingresados para determinar el lugar en la lista
#como salida muestra el lugar de la lista de la persona buscada en cuestion
