nombre=str(input("Ingrese su nombre: "))
sexo=str(input("Ingrese su sexo: "))
m="m"
f="f"

if sexo==m:
	print(nombre, "Es Hombre")
elif sexo==f:
	print(nombre, "Es Mujer") 
else:
	print("Su sexo no esta definido")

#programa base verifica el sexo del usuario siempre y cuando cumpla con las operaciones logicas