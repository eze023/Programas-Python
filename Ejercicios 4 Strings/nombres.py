print("Programas nombres ")

cadena="le lleva"
cadena2="años"
nombre=input("Ingrese su nombre y edad: ")
print()
nombre2=input("Ingrese su nombre y edad: ")
print()

for i in range(len(nombre)):
	if nombre[i]==" ":
		inicio=nombre[:i]
		edad=nombre[i:]

for i in range(len(nombre2)):
	if nombre2[i]==" ":
		fin=nombre2[:i]
		edad2=nombre2[i:]

edad=int(edad)
edad2=int(edad2)

if edad>edad2:
	total=edad-edad2
	total=str(total)
	print(inicio+" "+cadena+" "+total+" "+cadena2+" "+fin)

if edad2>edad:
	total=edad2-edad
	total=str(total)
	print(fin+" "+cadena+" "+total+" "+cadena2+" "+inicio)

print("Fin del programa")