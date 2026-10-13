# 87. Leer 10 números y determinar el mayor y menor. (Para + Si + Asignar)

class MayorMenor:
    def __init__(self, cantidad=10):
        self.cantidad = cantidad
        self.mayor = None
        self.menor = None

    def leer(self):
        for i in range(1, self.cantidad + 1):
            n = float(input(f"Número {i}: "))
            if self.mayor is None:
                self.mayor = n
                self.menor = n
            else:
                if n > self.mayor:
                    self.mayor = n
                if n < self.menor:
                    self.menor = n

    def mostrar(self):
        print(f"Mayor: {self.mayor}")
        print(f"Menor: {self.menor}")


if __name__ == "__main__":
    m = MayorMenor()
    m.leer()
    m.mostrar()
