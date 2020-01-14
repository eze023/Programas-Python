print("Programa promedio")

lista=[]
num1=0
suma=0
lugar=0
#Carga
for i in range(1,8):
	num1+=1
	lista+=[num1]
	suma+=num1
#Proceso
suma=suma/7
suma=int(suma)

lugar=lista.index(suma)

#Salida
print("Promedio: ",suma,"numeros mayores: ",lista[lugar+1:])

print("Fin del programa")

#de una lista generada aleatoriamente el programa sacara el promedio y mostrara en pantalla los numeros superiores al promedio