print("Programa mujeres en la lista")

lista_nombres=[]
lista_sexos=[]
indice=[]
#Carga
for i in range(8):
	nombre=str(input("Ingrese su nombre: "))
	nombre=nombre.lower()
	sexo=str(input("Ingrese su sexo m/f: "))
	sexo=sexo.lower()
	lista_nombres.append(nombre)
	lista_sexos.append(sexo)
#Proceso
for i in range(8):
	if lista_sexos[i]=="f":
		indice+=[lista_nombres[i]]
#Salida
print()
print("Las mujeres son: ",indice)
print()
print("Fin del programa")