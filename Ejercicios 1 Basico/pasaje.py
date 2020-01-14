print("Programa costo pasaje a cordoba")
print()

pasaje=400
nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))

if (edad>=5 and edad<=10):
	pasaje=pasaje*40
	pasaje=pasaje/100
	pasaje=400-pasaje
elif (edad>=65):
	pasaje=pasaje*40
	pasaje=pasaje/100
	pasaje=400-pasaje
else:
	pasaje=400

print("Nombre: ",nombre," Edad: ",str(edad),"Valor del pasaje: ",str(pasaje))