print("Programa salarios")

lista=[]
lista2=[]
lista3=[]
#Carga
datos=str(input("¿Hay datos? si/no: "))
datos=datos.lower()

while (datos=="si") or (datos=="s"):						#Carga de datos
	nombre=str(input("Ingrese el nombre del empleado: "))
	lista+=[nombre]
	salario=int(input("Ingrese su sueldo: "))
	lista2+=[salario]
	datos=str(input("¿Hay datos? si/no: "))
	datos=datos.lower()
	
#Proceso
for i in lista2[:]:											#Recorre la lista2 desde el rango 0 hasta el final de la lista
	if (i>15000):											#Si i(objeto de la lista) es mayor a 15000 entonces...
		lista3+=[(lista[lista2.index(i)])]					#Se guarda en la lista3 el nombre que corresponde al indice de la lista2 en el objeto (i)
#Salida
print()
print("Los empleados con salario superior a 15000 son: ",lista3[:])
print()
print("Fin del programa")