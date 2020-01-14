print("Programa digitos")

numero="1234567890"
i=len(numero)

while i > 3:
	i-=3
	numero=numero[:i] + '.' + numero[i:]

print()
print(numero)
print()
print("Fin del programa")

#el programa realiza el ingreso de un punto cada 3 cifras contando desde atras para adelante, teniendo en cuenta que este numero sea una cadena