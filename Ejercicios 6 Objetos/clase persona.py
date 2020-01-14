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

#el programa creamos una clase llamada persona donde ingresamos los datos de las personas y luego mostramos por pantalla los nombres con las edades cargadas