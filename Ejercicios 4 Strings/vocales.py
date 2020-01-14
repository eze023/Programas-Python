print("Programa vocales")

cadena="quiero comer manzanas, solamente manzanas"
vara=0
vare=0
vari=0
varo=0
varu=0


for i in range(len(cadena)):
	if cadena[i]=="a":
		vara+=1
	if cadena[i]=="e":
		vare+=1
	if cadena[i]=="i":
		vari+=1
	if cadena[i]=="o":
		varo+=1
	if cadena[i]=="u":
		varu+=1

if (vara>=vare) and (vara>=vari) and (vara>=varo) and (vara>=varu):
	print("La letra que mas se repite es: a ",vara)
if (vare>=vara) and (vare>=vari) and (vare>=varo) and (vare>=varu):
	print("La letra que mas se repite es: e ",vare)
if (vari>=vara) and (vari>=vare) and (vari>=varo) and (vari>=varu):
	print("La letra que mas se repite es: i ",vari)
if (varo>=vara) and (varo>=vare) and (varo>=vari) and (varo>=varu):
	print("La letra que mas se repite es: o ",varo)
if (varu>=vara) and (varu>=vare) and (varu>=vari) and (varu>=varo):
	print("La letra que mas se repite es: u ",varu)

print("Fin del programa")