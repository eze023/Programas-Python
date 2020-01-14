print("Programa datos")

datos=str(input("Hay datos? s/n: "))
datos=datos.lower()

while datos == "si":
	num=int(input("Ingrese un numero entero: "))
	if num<0:
		print("Es negativo")
	else:
		print("No es negativo")
	datos=input("Hay mas datos? s/n: ")

print("Fin del programa")