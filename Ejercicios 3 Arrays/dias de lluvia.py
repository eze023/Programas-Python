print("Dias de lluvia")

lluvia=[]
dias=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
suma=0
#Carga
for i in range(7):
	agua=int(input("Ingrese los milimetros de lluvia caida: "))
	lluvia+=[agua]
#Proceso
for i in lluvia:
	suma+=i
#Salida
print()
print("La mayor precipitacion de la semana fue el dia",dias[lluvia.index(max(lluvia))],"y la cantidad maxima de la semana fue: ",suma,".mm")
print()
print("Fin del programa")