print("Programa contador de letras")

probando=input("Ingrese una frase para calcular cuantas veces se repite una letra: ")

letra=input("Ingrese la letra que desea buscar: ")

contador=0

for i in range(len(probando)):
	if letra==probando[i]:
		contador+=1

print("La letra se repite: ", contador, " veces")

#el programa pide ingresar una frase, luego una letra que desea buscar de la frase que se ingreso
#este determinara la cantidad de veces que se repite la letra en la frase ingresada