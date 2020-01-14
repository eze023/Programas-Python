print("Calculo de sueldo")
print()

dias=int(input("Print escriba la cantidad de dias no trabajados: "))
anio=int(input("Ingrese el año de ingreso a la empresa: "))
sueldo=23000
porcentaje=0
actualidad=2019

actualidad=actualidad-anio

if (dias==0 and actualidad>=5):
	porcentaje=sueldo*30
	porcentaje=porcentaje/100
	sueldo=sueldo+porcentaje
	print("Su sueldo es: ", int(sueldo))
else:
	print("Su sueldo es: ",int(sueldo))

print("Fin del programa")