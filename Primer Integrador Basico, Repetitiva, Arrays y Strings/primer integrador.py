print("Practico 1")

lista_nombres=""
nombres=""
lista_sexo=[]
lista_edad=[]
edad1=""
nueva=""
cadena_nombr=""
nombr=""
ape=""
nom=""
var=""
acumulador=0
promedio=0
num=0

for i in range(7):
	nombre=str(input("Ingrese su nombre completo de la siguiente manera Apellido Nombre: "))
	nombres+=nombre
	for i in range(len(nombre)):
		if nombre[i]==" ":
			nom=nombre[i:i+2]
			ape=nombre[:i]
			var=nom+"."+ape
		if nombre[i]==" ":
			nombr+=nombre[i:]
	lista_nombres+=var
	sexo=input("Ingrese su sexo: ")
	sexo=sexo.lower()
	lista_sexo+=[sexo]
	edad=str(input("Ingrese su fecha de nacimiento dia/mes/año: "))
	for i in range(len(edad)):
		if edad[i]=="/":
			edad1=edad[i+1:]
	edad2=int(edad1)
	edad1=2019-edad2
	lista_edad+=[edad1]

cadena_nombr=nombr.split()

for i in range(len(cadena_nombr)):
	if len(cadena_nombr[i])>len(nueva):
		nueva=cadena_nombr[i]

for i in range(len(lista_sexo)):
	if lista_sexo[i]=="f":
		num+=1
		acumulador+=lista_edad[i]
		promedio=acumulador/num

print("Lista de las personas es:",lista_nombres)
print("El nombre mas largo es: ",nueva)
print("El promedio de edad de las mujeres es: ",promedio)