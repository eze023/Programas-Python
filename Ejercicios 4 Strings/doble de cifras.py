print("Programa valor doble de las cifras")

cadena="Juan tiene 25 años"
var=""

for i in range(len(cadena)):
	if cadena[i]=="0" or cadena[i]=="1" or cadena[i]=="2" or cadena[i]=="3" or cadena[i]=="4" or cadena[i]=="5" or cadena[i]=="6" or cadena[i]=="7" or cadena[i]=="8" or cadena[i]=="9":
		var+=cadena[i]

var=int(var)
var=var*2

print(var)