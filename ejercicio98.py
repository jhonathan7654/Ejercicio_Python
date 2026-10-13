# 98. Ingresar 10 notas, clasificar aprobadas/reprobadas y mostrar estadísticas.
class Estadisticas:
    def __init__(self, cantidad=10, nota_minima=60):
        self.cantidad = cantidad
        self.nota_minima = nota_minima
        self.notas = []
        self.aprobadas = 0
        self.reprobadas = 0

    def leer(self):
        for i in range(1, self.cantidad + 1):
            nota = float(input(f"Nota {i}: "))
            self.notas.append(nota)
            if nota >= self.nota_minima:
                self.aprobadas += 1
            else:
                self.reprobadas += 1

    def mostrar(self):
        print(f"Aprobadas: {self.aprobadas}")
        print(f"Reprobadas: {self.reprobadas}")
        print(f"Promedio: {sum(self.notas) / len(self.notas):.2f}")
        print(f"Mayor: {max(self.notas)}")
        print(f"Menor: {min(self.notas)}")
        print(f"% aprobación: {self.aprobadas / self.cantidad * 100:.1f}%")


if __name__ == "__main__":
    e = Estadisticas()
    e.leer()
    e.mostrar()
