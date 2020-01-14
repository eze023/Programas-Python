print("Programa costo pasaje a cordoba")
print()

pasaje=400
nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))

if (edad>=5 and edad<=10):
	descuento=100*0.4
	total=pasaje - descuento
elif (edad>=65):
	descuento=100*0.4
	total=pasaje - descuento
else:
	total=pasaje

print("Nombre: ",nombre," Edad: ",str(edad),"Valor del pasaje: ",str(total
))

#programa que aplica descuento en el pasaje de un viaje siempre y cuando sea de edad mayor a 5 y menor a 10
#o que sea de una persona mayor a 65 años
#en caso contrario se cobrara el valor total del boleto