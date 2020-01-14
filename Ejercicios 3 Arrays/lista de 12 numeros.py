print("Lista de 12 numeros")

lista=[]
suma=0
#Carga
for i in range(0,12):
	num=int(input("Ingrese un numero: "))
	lista+=[num]
#Proceso
for i in lista[:]:
	suma+=i

suma=suma/12
lista.append(suma)
#Salida
print()
print(lista[:])
print()
print("El promedio es: ",lista[12:])