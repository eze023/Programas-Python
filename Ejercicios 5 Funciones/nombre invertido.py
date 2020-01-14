
def nombreinvertido():
	nom=""
	ape=""
	nuevo=""
	nombre=str(input("Ingrese un nombre completo, Nombre y Apellido: "))
	for i in range(len(nombre)):
		if nombre[i]==" ":
			nom=nombre[i+1:]
			ape=nombre[:i]
			nuevo=nom+", "+ape

	return nuevo

print(nombreinvertido())

#el programa determina el a partir del ingreso del nombre y apellido, transfiere el apellido al inicio y separa por una coma