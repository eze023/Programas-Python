print("Programa para identificar cual es mayor")
print()

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1>num2:
	print()
	print("El primer numero " + str(num1) + " es mayor al segundo numero " + str(num2))
elif num2>num1:
	print()
	print("El segundo numero " + str(num2) + " es mayor que el primer numero " + str(num1))
else:
	print("Los numeros son iguales")

print()
print("Fin del programa")

#La funcion del programa es corroborar cual es el numero mayor
#en caso de que sean ambos numeros iguales el programa informara esto
