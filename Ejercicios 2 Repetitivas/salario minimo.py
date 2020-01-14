print("Salario Minimo")

valor_min=0

cantidad=int(input("Cuantos empleados tiene en la empresa: "))

lista=[]
lista2=[]

for i in range(cantidad):
	empleado=str(input("Escriba el nombre del empleado: "))
	salario=int(input("Ingrese el salario: "))
	lista+=[salario]
	lista2+=[empleado]
	valor_min=min(lista)

print("La persona que menos gana es", lista2[(lista.index(min(lista)))],"su salario es de $", valor_min)

#programa de bucle, pide ingresar la cantidad de personas que hay en existencia
#una vez ingresada la cantidad procede a pedir nombres y salarios
#al finalizar el programa determinara el salario mas bajo e imprimira en pantalla su nombre con el salario