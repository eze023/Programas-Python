print("Titulares de Argentina")
print()
#Listas
arqueros=["Sergio Romero", "Wilfredo Caballero", "Nahuel Guzman", "Franco Armani(T)"]
defensores=["Eduardo Salvio", "Gabriel Mercado(T)", "Nicolas Otamendi(T)", "Javier Mascherano", "Federico Fazio", "Marcos Rojo", "Marcos Acuna", "Nicolas Tagliafico(T)", 
"Ramiro Funes Mori", "German Pezzella(T)", "Cristian Ansaldi"]
mediocampistas=["Lucas Biglia", "Ever Banega", "Giovani Lo Celso(T)", "Manuel Lanzini", "Enzo Perez", "Pablo Perez", "Leandro Paredes(T)", "Guido Pizarro", "Rodrigo Battaglia", 
"Ricardo Centurion(T)", "Angel Di Maria", "Diego Perotti", "Maximiliano Meza"]
delanteros=["Paulo Dybala", "Sergio Aguero", "Gonzalo Higuain", "Lionel Messi(T)", "Mauro Icardi", "Lautaro Martinez(T)", "Cristian Pavon(T)"]
procYpos=["e-arq","e-arq","e-arq","l-arq",
"e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def",
"e-vol","e-vol","e-vol","e-vol","l-vol", "l-vol", "e-vol","e-vol","e-vol","l-vol","e-vol","e-vol","l-vol",
"e-del","e-del","e-del","e-del","e-del","l-del","l-del"]

#Variables
arq=""
arquero=""
defs=""
defensor=""
medio=""
mediocampo=""
mediocamp=""
dela=""
delantero=""
nueva=[]

#Funcion para extraer el arquero
for i in range(len(arqueros)):
	nombre=arqueros[i]
	for i in range(len(nombre)):
		if nombre[i]=="(":
			arq+=nombre[:i]+","

ka=arq.split()

for i in range(len(ka)):
	nombre=ka[i]
	for i in range(len(nombre)):
		if nombre[i]==",":
			arquero+=nombre[:i]+" "

print("Arquero:")
print(arquero)

#Funcion para extraer los apellidos de los defensores
for i in range(len(defensores)):
	nombre=defensores[i]
	for i in range(len(nombre)):
		if nombre[i]=="(":
			defs+=nombre[:i]+","

jota=defs.split()

for i in range(len(jota)):
	nombre=jota[i]
	for i in range(len(nombre)):
		if nombre[i]==",":
			defensor+=nombre[:i]+" "

print("Defensores:")
print(defensor)

#Funcion para extraer los apellidos de los mediocampistas
for i in range(len(mediocampistas)):
	nombre=mediocampistas[i]
	if nombre=="Giovani Lo Celso(T)":
		nombre="Giovani Lo.Celso(T)"
	for i in range(len(nombre)):
		if nombre[i]=="(":
			medio+=nombre[:i]+","

ele=medio.split()

for i in range(len(ele)):
	nombre=ele[i]
	for i in range(len(nombre)):
		if nombre[i]==",":
			mediocampo+=nombre[:i]+" "

mediocamp=mediocampo.replace("."," ",)

print("Mediocampistas:")
print(mediocamp)

#Funcion para extraer los apeliidos de los delanteros
for i in range(len(delanteros)):
	nombre=delanteros[i]
	for i in range(len(nombre)):
		if nombre[i]=="(":
			dela+=nombre[:i]+","

eme=dela.split()

for i in range(len(eme)):
	nombre=eme[i]
	for i in range(len(nombre)):
		if nombre[i]==",":
			delantero+=nombre[:i]+" "

print("Delanteros:")
print(delantero)

#Locales que no son mediocampistas
nueva=arqueros+defensores+mediocampistas+delanteros

print()
print("Locales que no son mediocampistas")
for i in range(len(procYpos)):
	if procYpos[i]=="l-arq" or procYpos[i]=="l-del":
		print(nueva[i])