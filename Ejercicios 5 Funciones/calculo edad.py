print("Ejercicio 12")

def cargadatos():
	nombres=[]
	fechas=[]
	carga="si"
	while carga!="no":
		nom=str(input("Ingrese su nombre: "))
		nombres+=[nom]
		fec=int(input("Ingrese su fecha de nacimiento: "))
		fechas+=[fec]
		carga=input("¿Desea cargar mas datos? si/no: ")

	return nombres, fechas

def calculoedad(lista, edades):
	mayor=0
	edad=[]
	nom=[]
	for i in range(len(edades)):
		mayor=2019-edades[i]
		if mayor>18:
			nom+=[lista[i]]

	return nom

listas, edad=cargadatos()
print()
print("Los mayores de edad son: ",calculoedad(listas, edad))

#el programa realiza la funcion de mostrar en pantalla las personas cuyo edad es mayor a 18 años