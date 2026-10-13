# 99. Leer N edades y determinar cuántas corresponden a niños, adolescentes, adultos y adultos mayores.
class ClasificadorEdades:
    def __init__(self):
        self.ninos = 0
        self.adolescentes = 0
        self.adultos = 0
        self.adultos_mayores = 0

    def clasificar(self, edad):
        if edad < 12:
            self.ninos += 1
        elif edad < 18:
            self.adolescentes += 1
        elif edad < 60:
            self.adultos += 1
        else:
            self.adultos_mayores += 1

    def mostrar(self):
        print(f"Niños: {self.ninos}")
        print(f"Adolescentes: {self.adolescentes}")
        print(f"Adultos: {self.adultos}")
        print(f"Adultos mayores: {self.adultos_mayores}")


if __name__ == "__main__":
    n = int(input("¿Cuántas edades va a ingresar? "))
    c = ClasificadorEdades()
    for i in range(1, n + 1):
        c.clasificar(int(input(f"Edad {i}: ")))
    c.mostrar()
