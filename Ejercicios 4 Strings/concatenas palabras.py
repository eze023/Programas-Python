print("Concatenar palabras")

cadena="Curso de Python"
cadena2="Programacion en "

posicion=cadena.find("Python")
principio=cadena[:posicion]
final=cadena[posicion:]

total=principio+cadena2+final

print(total)