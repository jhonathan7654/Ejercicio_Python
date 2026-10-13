# 96. Ingresar productos y precios hasta seleccionar Finalizar. Mostrar total.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def agregar(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar(self):
        print("\n--- RESUMEN ---")
        for p in self.productos:
            print(f"{p.nombre}: ${p.precio:.2f}")
        print(f"TOTAL: ${self.total:.2f}")


class Menu:
    def ejecutar(self):
        carrito = Carrito()
        while True:
            print("\n1. Agregar producto\n2. Finalizar")
            opcion = input("Opción: ")
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                carrito.agregar(Producto(nombre, precio))
            elif opcion == "2":
                carrito.mostrar()
                break
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
