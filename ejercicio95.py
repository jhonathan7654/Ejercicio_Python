# 95. Leer números hasta 0 y determinar pares, impares, positivos y negativos.
class AnalizadorNumeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0
        self.positivos = 0
        self.negativos = 0

    def analizar(self, n):
        if n % 2 == 0:
            self.pares += 1
        else:
            self.impares += 1
        if n > 0:
            self.positivos += 1
        elif n < 0:
            self.negativos += 1

    def mostrar(self):
        print(f"Pares: {self.pares}")
        print(f"Impares: {self.impares}")
        print(f"Positivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")


if __name__ == "__main__":
    a = AnalizadorNumeros()
    n = int(input("Número (0 para terminar): "))
    while n != 0:
        a.analizar(n)
        n = int(input("Número (0 para terminar): "))
    a.mostrar()
