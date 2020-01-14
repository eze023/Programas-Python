print("Ejercicio 2")

def reemplazo (pala, pala2, cade):
	nuevo=""
	for i in range(len(cade)):
		nuevo=cade.replace(pala, pala2,)
	return nuevo

print()
cadena="Quiero comer manzanas, solamente manzanas."
cade=cadena.lower()
print(cadena)
palabra="manzanas"
palabra1="peras"

print()
print(reemplazo(palabra, palabra1, cadena))