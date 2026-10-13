# 93. Solicitar notas de estudiantes hasta finalizar y calcular promedio, mayor y menor.
class RegistroNotas:
    def __init__(self):
        self.notas = []

    def agregar(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def mayor(self):
        return max(self.notas) if self.notas else None

    def menor(self):
        return min(self.notas) if self.notas else None


if __name__ == "__main__":
    registro = RegistroNotas()
    nota = float(input("Nota (negativo para finalizar): "))
    while nota >= 0:
        registro.agregar(nota)
        nota = float(input("Nota (negativo para finalizar): "))

    if registro.notas:
        print(f"Promedio: {registro.promedio():.2f}")
        print(f"Mayor: {registro.mayor()}")
        print(f"Menor: {registro.menor()}")
    else:
        print("No se ingresaron notas.")
