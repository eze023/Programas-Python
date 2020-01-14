print("Ejercicio 2- Guia 5")
print("Ingresar notas y devolver el promedio")
num=0
lista=[]
promedio=0

print("¿Cuantas notas desea ingresar?")
from Funciones.input import entero as i
num=i(num)

print()
print("Ingrese las notas")
from Funciones.cargarlista import cargalista as c
lista=c(num)

from Funciones.promedio import promedio as p
promedio=p(lista)

print()
print("El promedio es: ", promedio)

#Importamos las funciones para poder dar solucion a la problematica del programa