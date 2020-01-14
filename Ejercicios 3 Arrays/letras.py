print("Programa letras")

lista=[]
contador=0
#Carga
datos=input("Hay datos si/no: ")
datos=datos.lower()

while (datos=="si"):
	letra=str(input("Ingrese una letra: "))
	lista+=[letra]
	datos=input("Hay datos si/no: ")
	datos=datos.lower()
#Proceso
buscar=str(input("Ingrese una letra que desea buscar en la lista: "))

contador=lista.count(buscar)		#busca dentro de una lista cierto elemento
#Salida
print("La cantidad de veces que se repite la letra es: ",contador)
print()
print("Fin del programa")