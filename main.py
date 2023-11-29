print("Calculadora Made By Koan"
      "\n1.- Suma"
      "\n2.- Resta"
      "\n3.- Multiplicacion"
      "\n4.- Division"
      "\n5.- Modulo")
try:
    x = int(input("Ingrese la opcion que quiere que se realize :"))
except ValueError:
    print("Idiota, solo puedes meter una de las opciones anteriores.")
    exit(1)

if x >= 6:
    print("Opcion no valida")
    exit(1)
        

try:
    num1 = int(input("Introduce el primer numero aqui :"))
except ValueError:
    print("Idiota, solo puedes meter un numero.")
    exit(1)
    
try:   
    num2 = int(input("Introduce el segundo numero aqui :"))
except ValueError:
    print("Idiota, solo puedes meter un numero.")
    exit(1)

def sumar(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try: 
        return num1 / num2
    except ZeroDivisionError:
        print("Idiota no podes dividir entre 0")
        exit(1)            
def modulo(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        print("Idiota no podes dividir entre 0")
        exit(1) 

if x == 1: print("El resultado es: " + str(sumar(num1, num2)))
elif x == 2: print("El resultado es: " + str(resta(num1, num2)))
elif x == 3: print("El resultado es: " + str(multiplicacion(num1, num2)))
elif x == 4: print("El resultado es: " + str(division(num1, num2)))
elif x == 5: print("El resultado es: " + str(modulo(num1, num2)))
