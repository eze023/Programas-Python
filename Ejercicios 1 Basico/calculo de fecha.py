print("Programa periodo")
print("Ingrese un valor en segundos para calcular Dias, Horas, Minutos, Segundos")
num1=int(input("Ingrese un valor en segundos: "))
Days=0
Hours=0
Minutes=0

while num1>=60:
		num1=num1-60
		Minutes=Minutes+1

while Minutes>=60:
	Minutes=Minutes-60
	Hours=Hours+1

while Hours>=24:
	Hours=Hours-24
	Days=Days+1

print("Dias: ",str(Days),"Horas: ",str(Hours),"Minutos: ",str(Minutes),"Segundos: ",str(num1))

