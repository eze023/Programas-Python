print("Programa tabla ASCII a mayusculas")

pal=input("Ingrese una palabra: ")
pal2=""

for i in range(len(pal)):
	letra=ord(pal[i])
	letra=letra-32
	pal2+=chr(letra)

print(pal2)