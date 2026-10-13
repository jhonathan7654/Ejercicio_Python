# 97. Crear un menú bancario para consultar saldo, depositar, retirar y salir; validar fondos suficientes.
class CuentaBancaria:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def consultar(self):
        return self.saldo

    def depositar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        else:
            self.saldo += monto
            print("Depósito realizado.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        elif monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print("Retiro realizado.")


class Menu:
    def __init__(self):
        self.cuenta = CuentaBancaria(1000)

    def ejecutar(self):
        while True:
            print("\n--- BANCO ---")
            print("1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
            opcion = input("Opción: ")
            if opcion == "1":
                print(f"Saldo: ${self.cuenta.consultar():.2f}")
            elif opcion == "2":
                self.cuenta.depositar(float(input("Monto a depositar: ")))
            elif opcion == "3":
                self.cuenta.retirar(float(input("Monto a retirar: ")))
            elif opcion == "4":
                print("¡Gracias por usar el banco!")
                break
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
