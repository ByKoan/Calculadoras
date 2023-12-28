print("CalculadoraV1 Made By Koan")

a = int(input ("Numero1: ")) #Pedimos que nos ingrese el primer numero
b = int(input ("Numero2: ")) #Pedimos que nos ingrese el segundo numero
c = int(input ("Numero 1 - 4: ")) #Pedimos que nos ingrese un numero del 1 - 4

if c == 1: #Hacemos un if que dependiendo de la opcion que nos haya ingresado haga una operacion u otra
    # sumar
    print("El resultado de la suma es :" + str(a + b)) 
elif c == 2:
    # restas
    print("El resultado de la resta es :" + str( a - b))
elif c == 3:
    # division
    print("El resultado de la division es :"  + str(a / b))
elif c == 4:
    # multiplicacion
    print ("El resultado de la multiplicacion es :"  + str(a * b))
else:
    print("La opcion no estaba en el rango de 1 a 4") #La opcion no fue valida.
