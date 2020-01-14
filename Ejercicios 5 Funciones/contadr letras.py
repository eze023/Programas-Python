print("Ejercicio 3")

def contarletras(cade):
	nueva=""
	contador=0
	for i in range(len(cade)):
		if cade[i]!="," and cade[i]!="." and cade[i]!=" ":
			nueva+=cade[i]

	for i in range(len(nueva)):
		if nueva[i]:
			contador+=1
	return contador

cadena="Quiero comer manzanas, solamente manzanas."
print(cadena)
print("La cantidad de letras es: ",contarletras(cadena))