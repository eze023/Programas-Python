print("Ejercicio 6")

def lista():
	lista=[]
	for i in range(10):
		letra=input("Ingrese una letra: ")
		lista+=[letra]

	return lista

def cuenta(listaletras):
	contador=0
	for i in range(len(listaletras)):
		if listaletras[i] in "a, e, i, o, u":
			contador+=1

	return contador

vocales=lista()
print(vocales)
print("La cantidad de vocales es: ",cuenta(vocales))