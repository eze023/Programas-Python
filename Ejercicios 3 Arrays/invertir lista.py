print("Numeros al revez")

lista=[]
#Carga
datos=str(input("¿Hay datos? si/no: "))
datos=datos.lower()

while (datos=="si") or (datos=="s"):
	num1=int(input("Ingrese un numero: "))
	lista+=[num1]
	datos=str(input("¿Hay datos? si/no: "))
#Proceso
print()
lista.reverse()
#Salida
print(lista)
print()
print("Fin del programa")