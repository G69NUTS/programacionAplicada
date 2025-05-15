
def suma(): 
    def pedir_numeros():
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        return a, b

    a, b = pedir_numeros()
    return a + b
def resta():    
    def pedir_numeros():
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        return a, b

    a, b = pedir_numeros()
    return a - b

def multiplicacion():
    def pedir_numeros():
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        return a, b

    a, b = pedir_numeros()
    return a * b

def division():
    def pedir_numeros():
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        return a, b

    a, b = pedir_numeros()
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora con funciones")
    print("Opciones:\n suma = 1 \n restan = 2 \n multiplicacion = 3 \n division = 4")

    operacion = input("Elige una operación: ").lower()

    if operacion == "1":
        resultado = suma()
    elif operacion == "2":
        resultado = resta()
    elif operacion == "3":
        resultado = multiplicacion()
    elif operacion == "4":
        resultado = division()
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

calculadora()
