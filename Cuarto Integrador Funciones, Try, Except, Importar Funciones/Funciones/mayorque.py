def mayorque(lista, prome):
	mayores=[]
	num=0
	for i in range(len(lista)):
		num=lista[i]
		if num>prome:
			mayores+=[num]

	return mayores