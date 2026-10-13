# 92. Crear un menú de figuras geométricas y permitir calcular áreas repetidamente.
import math


class Figura:
    def area(self):
        raise NotImplementedError


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


class Menu:
    def ejecutar(self):
        while True:
            print("\n--- FIGURAS GEOMÉTRICAS ---")
            print("1. Círculo\n2. Cuadrado\n3. Rectángulo\n4. Triángulo\n5. Salir")
            opcion = input("Opción: ")
            if opcion == "5":
                print("¡Hasta luego!")
                break
            if opcion == "1":
                f = Circulo(float(input("Radio: ")))
            elif opcion == "2":
                f = Cuadrado(float(input("Lado: ")))
            elif opcion == "3":
                f = Rectangulo(float(input("Base: ")), float(input("Altura: ")))
            elif opcion == "4":
                f = Triangulo(float(input("Base: ")), float(input("Altura: ")))
            else:
                print("Opción inválida.")
                continue
            print(f"Área: {f.area():.2f}")


if __name__ == "__main__":
    Menu().ejecutar()
