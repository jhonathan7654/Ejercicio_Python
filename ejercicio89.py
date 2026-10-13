# 89. Leer N números y determinar cuántos son positivos, negativos y cero. (Para + Si)

class ClasificadorSigno:
    def __init__(self, n):
        self.n = n
        self.positivos = 0
        self.negativos = 0
        self.ceros = 0

    def leer(self):
        for i in range(1, self.n + 1):
            x = float(input(f"Número {i}: "))
            if x > 0:
                self.positivos += 1
            elif x < 0:
                self.negativos += 1
            else:
                self.ceros += 1

    def mostrar(self):
        print(f"Positivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")
        print(f"Ceros: {self.ceros}")


if __name__ == "__main__":
    n = int(input("¿Cuántos números va a ingresar? "))
    c = ClasificadorSigno(n)
    c.leer()
    c.mostrar()
