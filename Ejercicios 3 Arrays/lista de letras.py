print("Programa lista de letras")

contador=0
lista=[]
#Carga
for i in range(0,10):
	letra=str(input("Ingrese una letra: "))
	letra=letra.lower()
	lista+=[letra]
#Proceso
for i in lista[:]:
	if (i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u"):
		contador+=1
#Salida
print("La cantidad de letras vocales son: ", contador)
print()
print("Fin del programa")