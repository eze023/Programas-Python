print("Programa cantidad de autos")

precio=1
cantidad=0

while (precio>0):
	autos=str(input("Marca de auto: "))
	precio=int(input("Precio del auto: "))
	if (460000<=precio<=1250000):
		cantidad+=1


print("Hay ", cantidad,"Autos entre los precios de $460.000 y $1.250.000")