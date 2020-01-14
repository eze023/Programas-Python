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

print("La palabra mas larga contiene",len(palabra),"letras")

#el programa determina la cantidad de letras que contiene la palabra mas larga, compara en un bucle entre todas las palabras y luego una vez determinada comenzara a contar las letras en dicha palabra