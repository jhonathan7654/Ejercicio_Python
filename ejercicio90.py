# 90. Mostrar la tabla de multiplicar de un número y permitir repetir el proceso para diferentes números.
class TablaMultiplicar:
    def __init__(self, numero, limite=10):
        self.numero = numero
        self.limite = limite

    def mostrar(self):
        for i in range(1, self.limite + 1):
            print(f"{self.numero} x {i} = {self.numero * i}")


class Programa:
    def ejecutar(self):
        while True:
            n = int(input("Número para la tabla de multiplicar: "))
            TablaMultiplicar(n).mostrar()
            if input("¿Otro número? (S/N): ").strip().upper() != "S":
                break


if __name__ == "__main__":
    Programa().ejecutar()
