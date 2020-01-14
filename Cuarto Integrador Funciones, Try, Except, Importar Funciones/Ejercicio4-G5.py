print("Ejercicio 4 - Guia 5")
print("Listas sexo y nombres")
num=0
lista=[]

print("¿Cuantas personas desea cargar?")
from Funciones.input import entero as i
num=i(num)

print()
from Funciones.listanomsexo import cargadatos as c
nombres, sexo=c(num)

print()
from Funciones.mujeressolo import nombresmujeres as n
lista=n(nombres, sexo)

print("Los nombres de las mujeres son: ", lista)

#importamos las funciones a utilizar asignadas con una letra como variable