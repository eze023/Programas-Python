print("Pluviometro")
contador=0
pluviometro=0

for i in range(0,7):
	lluvia=float(input("Ingrese la cantidad de lluvia caida: "))
	pluviometro+=lluvia
	if lluvia<=0:
		contador+=1

print("La cantidad de lluvia de la semana es de: ", pluviometro,".mm la cantidad de dias que no llovio son: ",contador)

#Programa muestra la cantidad de lluvia caida en los dias, si algun dia se ingresa valor 0mm el contador sumara la cantidad de dias que no llovio