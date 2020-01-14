print("Programa suma de sueldos")
total=0
haydatos=input("Hay datos? si/no: ")

while haydatos=="si":
	sueldo=int(input("Ingrese su sueldo: "))
	total+=sueldo
	haydatos=input("Hay datos? si/no: ")

print("Sueldo total: ",total)
print()
print("Fin del programa")

#programa suma el valor total de los sueldos ingresados siempre y cuando el usuario ingrese que si hay datos