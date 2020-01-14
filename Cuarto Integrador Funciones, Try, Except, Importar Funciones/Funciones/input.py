def entero(n):
	while True:
		try:
			n=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("No es un numero entero intente nuevamente")
	return n

def reales(n):
	while True:
		try:
			n=float(input("Ingrese un numero: "))
			break
		except ValueError:
			print("No es un numero real intente nuevamente")
	return n
