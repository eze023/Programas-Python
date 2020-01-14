print("Valor maximo")
num=0
valor_max=0
carga=str(input("Desea ingresar un numero (si/ no): "))
carga=carga.lower()

while (carga!="no"):
	num=int(input("Ingrese un numero: "))
	carga=str(input("Hay mas numeros para cargar (si/no): "))
	if num>valor_max:
		valor_max=num
		
print()
print("Valor maximo: ", str(valor_max))
print("Fin del programa")