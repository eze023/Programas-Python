print("Programa para sacar total de mujeres")

cantidad=int(input("Ingrese la cantidad de personas a cargar: "))
contador=0
lista=[]

for i in range(cantidad):
	nombre=str(input("Ingrese su nombre: "))
	sexo=str(input("Masculino o Femenino m/f: "))
	sexo=sexo.lower()
	if (sexo=="f"):
		lista+=[nombre]
		contador+= 1
		
print()
print("Hay ", contador, "Mujeres")
print(lista)