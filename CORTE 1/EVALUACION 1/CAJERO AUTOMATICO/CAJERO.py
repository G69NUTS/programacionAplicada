saldo = 0.0  # Saldo inicial

def ingresar_dinero():
    global saldo
    cantidad = float(input("¿Cuánto deseas depositar? $"))
    if cantidad > 0:
        saldo += cantidad
        print(f" Se ingresaron ${cantidad:.2f}")
    else:
        print(" Monto inválido")

def retirar_dinero():
    global saldo
    cantidad = float(input("¿Cuánto deseas retirar? $"))
    if cantidad <= 0:
        print(" Monto inválido")
    elif cantidad > saldo:
        print(" Fondos insuficientes")
    else:
        saldo -= cantidad
        print(f" Se retiraron ${cantidad:.2f}")

def consultar_saldo():
    print(f"Tu saldo actual es: ${saldo:.2f}")

def menu():
    print("\n=== Cajero Automático ===")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

# Bucle principal del programa
while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ingresar_dinero()
    elif opcion == "2":
        retirar_dinero()
    elif opcion == "3":
        consultar_saldo()
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break
    else:
        print(" Opción inválida, intenta de nuevo.")

