print("Programa de hora")
num1= int(input("Ingrese la hora: "))
num2= int(input("Ingrese los minutos: "))
num3= int(input("Ingrese los segundos: "))

if num3>60:
	num3=num3-60
	num2=num2+1

if num2>60:
	num2=num2-60
	num1=num1+1

if num1>24:
	num1=num1-24

print()
print("Hora: ",num1,"minutos: ",num2,"segundos: ",num3)