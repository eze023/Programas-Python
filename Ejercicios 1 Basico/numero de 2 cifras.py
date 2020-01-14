print("Programa para calcular si un numero es positivo de dos cifras")
print()

num1=int(input("Ingrese el numero a calcular: "))

if 9<num1<100:
	print("El numero es positivo y de dos digitos: ",str(num1))
elif num1<0:
	print("El numero es negativo: ",str(num1))
else:
	print("El numero es superior a dos digitos: ",str(num1))