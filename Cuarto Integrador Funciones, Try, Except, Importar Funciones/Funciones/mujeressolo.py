def nombresmujeres(lista1, lista2):
	nom=[]
	for i in range(len(lista2)):
		if lista2[i]=="f":
			nom+=[lista1[i]]

	return nom