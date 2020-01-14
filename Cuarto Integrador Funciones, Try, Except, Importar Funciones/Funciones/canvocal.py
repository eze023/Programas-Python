def cuenta(listaletras):
	contador=0
	for i in range(len(listaletras)):
		if listaletras[i] in "a, e, i, o, u":
			contador+=1

	return contador