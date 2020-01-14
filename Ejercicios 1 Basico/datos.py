print("Programa Descuento en Electromecanica")
print()

name=str(input("Ingrese su nombre: "))
carrer=str(input("Ingrese la carrera en la que se inscribe: "))
city=str(input("Ingrese la ciudad donde vive: "))
payment=3000

if ((carrer == "electromecanica") and (city != "rio cuarto")):
	discount = 100*1.5
	total = payment - discount
	print("Tenes acceso al descuento de $", str(discount))
else:
	print("No Tenes acceso al descuento, tu cuota es de: ", str(total))

print()
print("Nombre: ",name, " Ciudad: ", city, " Carrera: ", carrer, " cuota: ", str(total))

#Este programa realiza un descuento en caso de ser correspondiente a la funcion logica
#aplica un descuento a los alumnos cuya carrera sea electromecanica y no sea oriundo de la ciudad de rio cuarto