print("Ejercicio 9")

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

def mayorque(lista, prome):
	mayores=[]
	num=0
	for i in range(len(lista)):
		num=lista[i]
		if num>prome:
			mayores+=[num]

	return mayores

numeros=[5, 2, 6, 8, 1, 4, 9]

prome=promedio(numeros)

print("El promedio es: ", prome)
print("Los numeros mayores al promedio es: ", mayorque(numeros, prome))