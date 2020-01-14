class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad


datos="si"
lista=[]
while datos=="si":
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    chaboncito=Persona(nombre, edad)
    lista+=[chaboncito]
    datos=input("Desea cargar mas datos?: si/no ")

for i in lista:
    print(i.nombre, i.edad)