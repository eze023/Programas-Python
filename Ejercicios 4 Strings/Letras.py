print("Programa letras")

cadena="River vuelve a las copas"
texto=""

for i in range(len(cadena)):
	if cadena[i] != "s":
		texto+=cadena[i]

print(texto)