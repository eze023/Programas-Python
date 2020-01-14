print("Ejercicio3 - Guia5")
print("Promedio y Numeros mayores al promedio")
num=0
lista=[]
promedio=0
mayores=0

print("¿Cuantas numeros desea ingresar?")
from Funciones.input import entero as i
num=i(num)

print()
print("Ingrese las notas")
from Funciones.cargarlista import cargalista as c
lista=c(num)

from Funciones.promedio import promedio as p
promedio=p(lista)

from Funciones.mayorque import mayorque as m
mayores=m(lista,promedio)

print()
print("El promedio es: ", promedio)
print()
print("Los mayores al promedio son: ", mayores)