# 85. Solicitar una respuesta S/N hasta obtener una opción válida.

class ValidadorSN:
    def __init__(self, mensaje="¿Desea continuar? (S/N): "):
        self.mensaje = mensaje

    def solicitar(self):
        while True:
            respuesta = input(self.mensaje).strip().upper()
            if respuesta in ("S", "N"):
                return respuesta
            print("Opción inválida. Ingrese S o N.")


if __name__ == "__main__":
    v = ValidadorSN()
    r = v.solicitar()
    print("Respondió:", "Sí" if r == "S" else "No")
