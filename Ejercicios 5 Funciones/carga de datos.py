print("Ejercicio 5")

def cargadedatos():
	lista=[]
	car="si"
	while car!="no":
		datos=input("Ingrese una palabra: ")
		lista+=[datos]
		carga=input("Desea seguir cargando datos? si/no: ")
		car=carga.lower()

	return lista

def palabralarga(lista):
	larga=""
	cantidad=0
	for i in range(len(lista)):
		pala=lista[i]
		if len(pala)>len(larga):
			larga=pala
			cantidad=len(larga)

	return larga, cantidad

listapalabras=cargadedatos()
print()
print("La palabra mas larga es: ",palabralarga(listapalabras), "letras")