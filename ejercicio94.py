# 94. Registrar edades hasta ingresar 0 y determinar cantidad de mayores y menores.
class RegistroEdades:
    def __init__(self, mayoria_edad=18):
        self.mayoria_edad = mayoria_edad
        self.mayores = 0
        self.menores = 0

    def registrar(self, edad):
        if edad >= self.mayoria_edad:
            self.mayores += 1
        else:
            self.menores += 1

    def mostrar(self):
        print(f"Mayores de edad: {self.mayores}")
        print(f"Menores de edad: {self.menores}")


if __name__ == "__main__":
    r = RegistroEdades()
    edad = int(input("Edad (0 para terminar): "))
    while edad != 0:
        r.registrar(edad)
        edad = int(input("Edad (0 para terminar): "))
    r.mostrar()
