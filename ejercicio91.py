# 91. Crear una calculadora que permita realizar operaciones hasta seleccionar Salir.
class Calculadora:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b


class Menu:
    def __init__(self):
        self.calc = Calculadora()

    def mostrar(self):
        print("\n--- CALCULADORA ---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = input("Opción: ")
            if opcion == "5":
                print("¡Hasta luego!")
                break
            if opcion not in ("1", "2", "3", "4"):
                print("Opción inválida.")
                continue
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            try:
                if opcion == "1":
                    r = self.calc.sumar(a, b)
                elif opcion == "2":
                    r = self.calc.restar(a, b)
                elif opcion == "3":
                    r = self.calc.multiplicar(a, b)
                else:
                    r = self.calc.dividir(a, b)
                print("Resultado:", r)
            except ZeroDivisionError as e:
                print("Error:", e)


if __name__ == "__main__":
    Menu().ejecutar()
