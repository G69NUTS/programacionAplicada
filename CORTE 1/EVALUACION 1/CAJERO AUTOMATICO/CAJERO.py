class Cajero:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"El saldo de {self.nombre} es: {self.saldo}")

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No hay suficiente saldo.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo}")
