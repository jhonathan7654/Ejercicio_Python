# 86. Leer 10 números y determinar cuántos son pares y cuántos impares. (Para + Si)

class ContadorParesImpares:
    def __init__(self, cantidad=10):
        self.cantidad = cantidad
        self.pares = 0
        self.impares = 0

    def leer_y_contar(self):
        for i in range(1, self.cantidad + 1):
            n = int(input(f"Número {i}: "))
            if n % 2 == 0:
                self.pares += 1
            else:
                self.impares += 1

    def mostrar(self):
        print(f"Pares: {self.pares}")
        print(f"Impares: {self.impares}")


if __name__ == "__main__":
    c = ContadorParesImpares()
    c.leer_y_contar()
    c.mostrar()
