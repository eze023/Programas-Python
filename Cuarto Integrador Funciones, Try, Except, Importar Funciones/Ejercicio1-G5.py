print("Ejercicio 1 - Guia 1")
print("Ingrese valores para sumarlos")
num1=0
num2=0
total=0

from Funciones.input import entero as i
num1=i(num1)

from Funciones.input import entero as i
num2=i(num2)

from Funciones.suma import suma as s
total=s(num1,num2)

print("El total es: ",total)