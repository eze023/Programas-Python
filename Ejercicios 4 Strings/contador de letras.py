print("Programa contador de letras")

probando=input("Ingrese una frase para calcular cuantas veces se repite una letra: ")

letra=input("Ingrese la letra que desea buscar: ")

contador=0

for i in range(len(probando)):
	if letra==probando[i]:
		contador+=1

print("La letra se repite: ", contador, " veces")