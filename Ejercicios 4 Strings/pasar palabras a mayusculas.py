print("Programa tabla ASCII a mayusculas")

pal=input("Ingrese una palabra: ")
pal2=""

for i in range(len(pal)):
	letra=ord(pal[i])
	letra=letra-32
	pal2+=chr(letra)

print(pal2)

#Ingresamos una palabra por consola y a traves del programa transforma la palabra a mayusculas
#a pesar de que python tiene una funcion la cual transforma la palabras a mayusculas nos hacemos valer por una funcion generada para realizar la misma funcion