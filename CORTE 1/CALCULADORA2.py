def pedir_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

def suma():
    a, b = pedir_numeros()
    return a + b

def resta():
    a, b = pedir_numeros()
    return a - b

def multiplicacion():
    a, b = pedir_numeros()
    return a * b

def division():
    a, b = pedir_numeros()
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

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
