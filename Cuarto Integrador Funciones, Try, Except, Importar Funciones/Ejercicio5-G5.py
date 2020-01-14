print("Ejercicio 5 - Practico 5")
print("Cantidad de vocales")
num=0
lista=[]
cantidad=0

print("¿Cuantas letras desea ingresar?")
from Funciones.input import entero as i
num=i(num)

from Funciones.listaletras import lista as l
lista=l(num)

from Funciones.canvocal import cuenta as c
cantidad=c(lista)

print("La cantidad de volcales es: ", cantidad)