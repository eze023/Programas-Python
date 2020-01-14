print("Ejercicio 11")

def diassemana():
	lista=[]
	dias=["Domingo","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
	acumulador=0
	for i in range(len(dias)):
			dia=int(input("Ingrese la cantidad de lluvia caida el " + dias[i] + ": "))
			lista+=[dia]
			acumulador+=dia

	return lista, dias, acumulador

def lluvia(lista, dias):
	mayor=0
	dia=""
	for i in range(len(lista)):
		if mayor<lista[i]:
			mayor=lista[i]
			dia=dias[i]

	return dia, mayor

agua, dias, total=diassemana()

dia, cantidad=lluvia(agua, dias)

print("El dia que mas llovio fue el ", dia, "con un total de", cantidad, "y en la semana llovio",total, "mm")

#el programa utiliza una funcion para determinar el dia que mas llovio y el total de milimetros caidos en la semana