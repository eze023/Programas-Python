print("Programa Datos")
print()

name=str(input("Ingrese su nombre: "))
carrer=str(input("Ingrese la carrera en la que se inscribe: "))
city=str(input("Ingrese la ciudad donde vive: "))
payment=3000

if ((carrer == "electromecanica") and (city != "rio cuarto")):
	payment=3000*15
	payment=payment/100
	payment=3000-payment
	print("Tenes acceso al descuento", str(payment))
else:
	print("No Tenes acceso al descuento, tu cuota es de: ", str(payment))

print()
print("Nombre: ",name, " Ciudad: ", city, " Carrera: ", carrer, " cuota: ", str(payment))