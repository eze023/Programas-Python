print("Programa edad")

personas=int(input("¿Cuantas personas se van a cargar en el sistema?: "))
promedio=0

for i in range(personas):
	edad=int(input("Ingrese su edad: "))
	promedio+=edad

promedio=promedio/personas
print()
print("La edad promedio es: ", promedio)