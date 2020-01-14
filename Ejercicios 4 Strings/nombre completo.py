print("Programa nombre completo")

nombre=input("Ingrese su nombre completo: ")
cadena=""
cadena2=""

for i in range(len(nombre)):
	if nombre[i]==" ":
		cadena+=nombre[i:]
		cadena2+=nombre[:i]


print(cadena+","+cadena2)

#El programa realiza una funcionalidad de cambiar de lugar el apellido por el nombre y separa ambos por una coma