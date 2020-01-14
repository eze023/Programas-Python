print("Programa de promedio de notas")
print("")

num1 = int(input("Ingrese su primera nota: "))
num2 = int(input("Ingrese su segunda nota: "))
num3 = int(input("Ingrese su tercera nota: "))

def promedio(n1, n2, n3):
	n4=(n1+n2+n3)/3
	print("")
	print("Su promedio es: " + str(n4))

promedio(num1, num2, num3)

#programa que calcula el promedio de las notas