# 100. Crear un menú para factorial, tabla de multiplicar, paridad y cuadrado; repetir hasta Salir.
class Operaciones:
    @staticmethod
    def factorial(n):
        if n < 0:
            return None
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    @staticmethod
    def tabla(n):
        return [f"{n} x {i} = {n * i}" for i in range(1, 11)]

    @staticmethod
    def paridad(n):
        return "par" if n % 2 == 0 else "impar"

    @staticmethod
    def cuadrado(n):
        return n ** 2


class Menu:
    def ejecutar(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Factorial\n2. Tabla de multiplicar\n3. Paridad\n4. Cuadrado\n5. Salir")
            opcion = input("Opción: ")
            if opcion == "5":
                print("¡Hasta luego!")
                break
            if opcion not in ("1", "2", "3", "4"):
                print("Opción inválida.")
                continue
            n = int(input("Número: "))
            if opcion == "1":
                r = Operaciones.factorial(n)
                print(f"{n}! = {r}" if r is not None else "No existe factorial de negativos.")
            elif opcion == "2":
                print("\n".join(Operaciones.tabla(n)))
            elif opcion == "3":
                print(f"{n} es {Operaciones.paridad(n)}")
            else:
                print(f"{n}² = {Operaciones.cuadrado(n)}")


if __name__ == "__main__":
    Menu().ejecutar()
