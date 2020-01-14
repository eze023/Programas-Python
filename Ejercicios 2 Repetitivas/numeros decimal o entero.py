print("Programa numeros")

for i in range(0,7):
	num=input("Ingrese un numero: ")
	if '.' in num:
		print("Numero decimal: ",num)
	else:
		print("Numero entero: ",num)

print("Fin del programa")