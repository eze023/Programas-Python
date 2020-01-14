print("Programa letras")

cadena="Boca vuelve a las copas"
texto=""

for i in range(len(cadena)):
	if cadena[i] != "s":
		texto+=cadena[i]

print(texto)

#el programa esta determinado a eliminar de la cadena la letra S para luego crear una cadena nueva y mostrarla en pantalla