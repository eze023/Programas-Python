print("Programa busqueda")

cadena="quiero comer manzanas, solamente manzanas"
contador=0
i=0
print("Quiero comer manzanas, solamente manzanas")
print()

buscar=input("Ingrese la palabra que desea buscar de la frase anterior: ")
buscar=buscar.lower()

contador=cadena.count(buscar)

print()
if contador>0:
	print("La palabra se encuentra",contador,"veces")
else:
	print("No se encontro la palabra ingresada")

print()
print("Fin del programa")