print("Programa nombre completo")

nombre=input("Ingrese su nombre completo: ")
cadena=""
cadena2=""

for i in range(len(nombre)):
	if nombre[i]==" ":
		cadena+=nombre[i:]
		cadena2+=nombre[:i]


print(cadena+","+cadena2)