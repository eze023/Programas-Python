print("Programa de cantidad de letras")

cadena="quiero comer manzanas, solamente manzanas."
vacio=""
palabra=""

for i in range(len(cadena)):
	if cadena[i]!="," and cadena[i]!=".":
		vacio+=cadena[i]

cadena1=vacio.split()

for i in cadena1:
	if len(i)>len(palabra):		#len(i)= i equivale a la palabra
		palabra=i

print(len(palabra))