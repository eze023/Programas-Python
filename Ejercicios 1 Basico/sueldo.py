print("Calculo de sueldo")
print()

dias=int(input("Print escriba la cantidad de dias no trabajados: "))
anio=int(input("Ingrese el año de ingreso a la empresa: "))
sueldo=23000
actualidad=2020

actualidad=actualidad-anio

if (dias==0 and actualidad>=5):
	porcentaje=sueldo*0.3
	sueldo=sueldo+porcentaje
	print("Su sueldo es: ", int(sueldo))
else:
	print("Su sueldo es: ",int(sueldo))

print("Fin del programa")

#Calcula el adicional al sueldo si este no falto ningun dia al trabajo y su tiempo de trabajo es superior a 5 años en la empresa