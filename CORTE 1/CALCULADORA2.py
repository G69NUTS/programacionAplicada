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
    print("Calculadora con funciones en Python")
    print("Opciones: suma, resta, multiplicacion, division")

    operacion = input("Elige una operación: ").lower()

    if operacion == "suma":
        resultado = suma()
    elif operacion == "resta":
        resultado = resta()
    elif operacion == "multiplicacion":
        resultado = multiplicacion()
    elif operacion == "division":
        resultado = division()
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

# Ejecutar la calculadora
calculadora()
