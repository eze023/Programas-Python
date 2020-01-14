print("Programa contador")
contador=0

for i in range(10):
	num1=int(input("Ingrese un numero: "))
	if (num1>23):
		contador+=1

print("Hay ", contador," Numeros mayores que 23")
print("Fin del programa")

#el programa pedira ingresar 10 numeros
#aquellos numeros que sean superiores a 23 seran cargados a un contador
#una vez finalizado este mostrara la cantidad de numeros que son mayores a 23