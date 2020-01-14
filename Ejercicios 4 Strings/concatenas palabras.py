print("Concatenar palabras")

cadena="Curso de Python"
cadena2="Programacion en "

posicion=cadena.find("Python")
principio=cadena[:posicion]
final=cadena[posicion:]

total=principio+cadena2+final

print(total)

#el programa de dos cadenas las concatenara a partir de una posicion determinada y formara la frase que se muestra en pantalla