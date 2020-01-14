def repeticion(cade, letra):
	contador=0
	for i in range(len(cade)):
		if letra==cade[i]:
			contador+=1
	return contador

print()
cadena="Quiero comer manzanas, solamente manzanas."
cade=cadena.lower()
print(cadena)
print()
letra=str(input("Ingrese una letra que desea buscar: "))

print("Las veces que aparece la letra es: ",repeticion(cade, letra))

#el programa realiza la funcion de buscar y contar la cantidad de veces que se repite la letra en la frase ya preestablecida