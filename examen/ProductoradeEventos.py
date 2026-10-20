class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            print("La pila está vacía")
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            print("La cola está vacía")
            return None
        return self.items.pop(0)

# Agrega tus pruebas debajo. Usa los datos asignados en tu versión.

# ---------------- PRUEBAS (Versión 25: Productora de eventos) ----------------
datos = [("EV01", "Sonido"), ("EV02", "Luces"), ("EV03", "Escenario")]

lista = ListaEnlazada()
pila = Pila()
cola = Cola()

for codigo, descripcion in datos:
    lista.agregar(codigo, descripcion)
    cola.encolar(f"{codigo}: {descripcion}")
    pila.apilar(f"{codigo}: {descripcion}")

print("=== Lista enlazada (recorrido) ===")
lista.mostrar()

print("\n=== FIFO en la cola (sale primero el primero agregado) ===")
for _ in range(3):
    print("Desencolado:", cola.desencolar())
cola.desencolar()  # prueba de cola vacía

print("\n=== LIFO en la pila (sale primero el último agregado) ===")
for _ in range(3):
    print("Desapilado:", pila.desapilar())
pila.desapilar()  # prueba de pila vacía

# ---------------- RETO INDIVIDUAL ----------------
# Verifica que deshacer no borre el registro enlazado.
print("\n=== Reto individual: deshacer no borra el registro enlazado ===")
pila_deshacer = Pila()
for codigo, descripcion in datos:
    pila_deshacer.apilar(codigo)

print("Deshacer ->", pila_deshacer.desapilar())  # solo quita de la pila

contador = 0
actual = lista.cabeza
while actual is not None:
    contador += 1
    actual = actual.siguiente

print("Nodos en la lista después de deshacer:", contador)
assert contador == 3, "Error: deshacer borró nodos de la lista enlazada"
print("OK: la lista enlazada sigue intacta")
lista.mostrar()
