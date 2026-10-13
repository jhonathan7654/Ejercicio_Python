# 88. Leer N números y calcular suma y promedio. (Para + acumulador)

class SumaPromedio:
    def __init__(self, n):
        self.n = n
        self.suma = 0.0

    def leer(self):
        for i in range(1, self.n + 1):
            self.suma += float(input(f"Número {i}: "))

    @property
    def promedio(self):
        return self.suma / self.n if self.n > 0 else 0

    def mostrar(self):
        print(f"Suma: {self.suma}")
        print(f"Promedio: {self.promedio:.2f}")


if __name__ == "__main__":
    n = int(input("¿Cuántos números va a ingresar? "))
    s = SumaPromedio(n)
    s.leer()
    s.mostrar()
