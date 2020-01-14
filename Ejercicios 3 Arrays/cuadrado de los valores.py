print("Programa Cuadrado de valores")

lista=[]
lista2=[]
num2=0
#Carga
datos=str(input("¿Hay datos? si/no: "))
datos=datos.lower()

while (datos=="si") or (datos=="s"):
	num1=int(input("Ingrese un numero: "))
	lista+=[num1]
	datos=str(input("¿Hay datos? si/no: "))
	datos=datos.lower()	
#Proceso
for i in lista[:]:
	lista2.append(i**2)	#inserta en la lista2 el cuadrado de los numeros ingresados donde i(lugar) donde se encuentra el primer objeto
#Salida
print()
print(lista2[:])
print()
print("Fin del programa")

#el programa pide ingresar cierta cantidad de numeros al finalizar el trabajo este tomara valor por valor sacara el cuadrado del mismo y lo guardara en otra lista