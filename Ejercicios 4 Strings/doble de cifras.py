print("Programa valor doble de las cifras")

cadena="Juan tiene 25 años"
var=""

for i in range(len(cadena)):
	if cadena[i] in "1234567890":
		var+=cadena[i]

var=int(var)
var=var*2

print("El valor es: ",var)

#El programa determina y nos muestra como eliminar un texto de una cadena tomar el valor y multiplicarlo para mostrar su salida en pantalla