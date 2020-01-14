print("Programa calculo matematico")
print()
n1=int(input("Ingrese el primer numero: "))
print()
n2=int(input("Ingrese el segundo numero: "))
print()
operation=str(input("Ingrese la operacion a realizar con + ó -: "))
s="+"
r="-"

def plus(num1, num2):
    num3=num1+num2
    print()
    print("La suma es: " + str(num3))

def substraction(num1, num2):
    num3=num1-num2
    print()
    print("La resta es: " + str(num3))

if operation==s:
    plus(n1,n2)
elif operation==r:
    substraction(n1,n2)
else:
    print("El simbolo ingresado no corresponde a ninguna operacion valida")

#Programa de calculos matematicos
#Es un programa basico que realiza suma o resta, en caso de pedir otra operacion este informara que no corresponde a una operacion valida