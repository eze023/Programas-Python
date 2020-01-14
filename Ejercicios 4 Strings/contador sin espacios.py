print("Programa contador sin separadores")

cadena="quiero comer manzanas, solamente manzanas"
nueva=""

for i in range(len(cadena)):
	if cadena[i]!=" ":
		nueva+=cadena[i]

print("Cadena queda asi:", nueva)
print("La cantidad de caracteres es de:",len(nueva))

#a partir de una cadena determinada en una variable, el programa determinara la cantidad de letras y caracteres ingresados en la cadena
#esta cuenta se realizara sin espacios
