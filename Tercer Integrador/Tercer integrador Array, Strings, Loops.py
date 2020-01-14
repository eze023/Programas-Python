print("Practico3")

movies=["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
         "Dumb & Dumber(1994)com", "Blade Runner 2049(1982)sf"]

nombres=[]
año=[]
tipo=[]
tipo2=[]
contador=0

for i in range(len(movies)):
	peli=movies[i]
	for i in range(len(peli)):
		if peli[i]=="(":
			nombres+=[peli[:i]]

for i in range(len(movies)):
	num=movies[i]
	for i in range(len(num)):
		if num[i]=="(":
			año+=[num[i+1:i+5]]

for i in range(len(movies)):
	tp=movies[i]
	for i in range(len(tp)):
		if tp[i]==")":
			tipo+=[tp[i+1:]]

for i in range(len(tipo)):
	if tipo[i]=="sf":
		tipo2+=["Ciencia Ficcion"]
	if tipo[i]=="com":
		tipo2+=["Comedia"]
	if tipo[i]=="act":
		tipo2+=["Accion"]

for i in range(len(tipo)):
	if tipo[i]=="sf":
		sf="Ciencia Ficcion"
		print(sf+":"+" "+nombres[i])

for i in range(len(año)):
	agno=año[i]
	agno=int(agno)
	if agno<2000:
		contador+=1
print("Peliculas estrenadas antes del año 2000:",contador)

letra=str(input("Ingrese una letra para buscar una pelicula correspondiente: "))
letra=letra.upper()

for i in range(len(nombres)):
	nombr=nombres[i]
	agno=año[i]
	tip=tipo2[i]
	for i in range(len(nombr)):
		if nombr[i]==letra and nombr[i+5]!="r":
			inicio=nombr[i:]
			print(inicio+" "+agno+" "+tip)

#el programa realiza la funcion de mostrar en pantalla las peliculas de ciencia ficcion y la cantidad de peliculas cuyo estreno fue anterior al año 2000, ademas pide al usuario ingresar una lista para verificar si la pelicula esta en la lista