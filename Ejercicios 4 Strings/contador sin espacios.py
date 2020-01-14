print("Programa contador sin separadores")

cadena="quiero comer manzanas, solamente manzanas"
nueva=""

for i in range(len(cadena)):
	if cadena[i]!=" ":
		nueva+=cadena[i]

print("Cadena queda asi:", nueva)
print("La cantidad de caracteres es de:",len(nueva))