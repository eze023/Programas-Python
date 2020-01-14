print("Ejercicio 1")

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

print(repeticion(cade, letra))