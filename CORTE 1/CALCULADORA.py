def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

def calculadora():
    print("Calculadora en Python")
    print("Operaciones: suma, resta, multiplicacion, division")
    
    op = input("Ingresa la operación: ").lower()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if op == "suma":
        print("Resultado:", suma(a, b))
    elif op == "resta":
        print("Resultado:", resta(a, b))
    elif op == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif op == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida")

calculadora()
