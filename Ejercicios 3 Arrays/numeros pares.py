print("Programa numeros pares")

lista=[]
#Carga 
for i in range(0,31):					#Proceso
	if (i>0) and (i<31) and (i%2==0):	#la variable i % 2(resto) igual a 0 entonces.. 
		lista+=[i]
#Salida
print(lista[:])
print("Fin del programa")