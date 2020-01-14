class Operacion():
    def __init__(self):
        self.num1=int(input("Ingrese el primer numero: "))
        self.num2=int(input("Ingrese el segundo numero: "))

    def total(self):
        self.total=0
        return self.total
    
    def salida(self):
        print("El total de la operacion es:",self.total)

class Suma(Operacion):
    def suma(self):
        self.total=self.num1+self.num2

class Promedio(Operacion):
    def promedio(self):
        self.total=(self.num1+self.num2)/2

opera=Suma()
opera.suma()
opera.salida()
print()
print("------------------------------")
print()
opera=Promedio()
opera.promedio()
opera.salida()

#Creamos una clase llamada operacion donde en su funcionamiento nos dedicamos a tomar los datos inicializados luego realizar la funcion al cual se necesita, por un lado llamamos una suma por otro lado el promedio