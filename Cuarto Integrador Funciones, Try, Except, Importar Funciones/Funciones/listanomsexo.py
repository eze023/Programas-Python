def cargadatos(n):
	nombres=[]
	sexo=[]
	for i in range(n):
		nombre=input("Ingrese su nombre: ")
		nombres+=[nombre]
		sexos=input("Ingrese su sexo m/f: ")
		sexo+=sexos

	return nombres, sexo