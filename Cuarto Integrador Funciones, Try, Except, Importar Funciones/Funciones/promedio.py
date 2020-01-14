def promedio(lista):
	acumulador=0
	num=0
	promedio=0
	cantidad=0
	for i in range(len(lista)):
		num=lista[i]
		acumulador+=num
		cantidad+=1
	promedio=acumulador/cantidad

	return promedio