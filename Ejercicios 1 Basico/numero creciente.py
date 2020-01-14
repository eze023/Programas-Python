print("Prgrama mostrar numeros crecientes")
print()

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1>num2:
	print()
	print(num2,",", num1)
elif num1<num2:
	print()
	print(num1, ",", num2)
else:
	print()
	print("Los numeros son iguales")
	print(num1, ",", num2)

print()
print("Fin del programa")

#programa ordena los numeros de menor a mayor, en caso de ser iguales imprime ambos numeros