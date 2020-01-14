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