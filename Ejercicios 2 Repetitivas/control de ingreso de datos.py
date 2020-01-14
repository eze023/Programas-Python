print("Programa datos")

datos=str(input("Hay datos? s/n: "))
datos=datos.lower()

while datos == "si" or datos == "s":
	num=int(input("Ingrese un numero entero: "))
	if num<0:
		print("Es negativo")
	else:
		print("No es negativo")
	datos=input("Hay mas datos? s/n: ")

print("Fin del programa")

#programa de repetitivas, pregunta si hay datos para cargar en caso de carga, pedira un numero
#este determina si el numero es positivo o no