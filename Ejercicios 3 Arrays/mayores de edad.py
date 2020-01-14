print("Mayores de edad")

nombres=[]
fechas=[]
indice=[]
agno=0
#Carga
datos=str(input("¿Hay datos? si/no: "))
datos=datos.lower()

while (datos=="si") or (datos=="s"):
	nomb=str(input("Ingrese su nombre: "))
	fech=int(input("Ingrese su año de nacimiento: "))
	nombres+=[nomb]
	fechas+=[fech]
	datos=str(input("¿Hay datos? si/no: "))
	datos=datos.lower()
#Proceso
for i in fechas[:]:	#desde i=0 hasta el final de la lista fechas
	agno=2019-i		#la fecha ingresada en i en lista fechas, se resta de 2019
	if (agno>=18):	#si la resta de 2019 de la lista i es mayor a 18 entonces
		indice+=[(nombres[(fechas.index(i))])]	#ingresa a la lista indice los nombres de las personas mayores de 18
#Salida
print()
print("Las personas mayores de edad son: ",indice)
print()
print("Fin del programa")