nombre=str(input("Ingrese su nombre: "))            #comentario 1 toma de nombre
num1=int(input("Ingrese su edad: "))                #comentario 2 toma de edad

if 5<num1<18:
    print("Su nombre es: ", nombre, "Su edad es: ", str(num1), "Es menor de edad")
elif 18<=num1<100:
    print("Su nombre es: ", nombre, "Su edad es: ", str(num1), "Puede pasar")
else:
    print("Su edad no es real")