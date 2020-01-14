print("Programa busqueda de nombres")

lugar=0
lista=[]
#Carga
datos=str(input("¿Quiere ingresar un nombre?: "))
datos=datos.lower()

while datos=="si":
	nombre=str(input("Ingrese un nombre: "))
	lista+=[nombre]
	datos=str(input("¿Quiere ingresar un nombre?: "))
	datos=datos.lower()
#Proceso
nom=str(input("Ingrese el nombre que desea buscar: "))

lugar=lista.index(nom) #lugar en la lista
#Salida
print("El lugar de la lista es: ",format(lugar)) #da formato al lugar donde esta el nombre
print()
print("Fin del programa")