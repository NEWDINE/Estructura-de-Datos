# ===============================================================
# Programa: Suma de dos colas
# Autor: [Tu nombre]
# Descripción:
# Este programa crea dos colas (A y B), permite al usuario ingresar
# sus elementos, y genera una tercera cola (C) que contiene la suma
# elemento a elemento de A y B. Finalmente, muestra las tres colas
# en forma vertical.
# ===============================================================

# ---------------------------------------------------------------
# Clase Cola
# ---------------------------------------------------------------
class Cola:
    """Implementación básica de una cola (FIFO)"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

# ---------------------------------------------------------------
# Función para sumar dos colas
# ---------------------------------------------------------------
def sumar_colas(cola_a, cola_b):
    cola_c = Cola("C")
    tam = min(len(cola_a), len(cola_b))  # suma hasta el menor tamaño
    for i in range(tam):
        suma = cola_a[i] + cola_b[i]
        cola_c.encolar(suma)
    return cola_c

# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print("=== SUMA DE DOS COLAS ===")
cola_a = Cola("A")
cola_b = Cola("B")

# Ingreso de datos
n = int(input("¿Cuántos elementos tendrá cada cola?: "))

print("\n--- Ingrese los elementos de la Cola A ---")
for i in range(n):
    valor = int(input(f"A[{i+1}]: "))
    cola_a.encolar(valor)

print("\n--- Ingrese los elementos de la Cola B ---")
for i in range(n):
    valor = int(input(f"B[{i+1}]: "))
    cola_b.encolar(valor)

# Suma de las colas
cola_c = sumar_colas(cola_a, cola_b)

# ---------------------------------------------------------------
# Despliegue en forma vertical
# ---------------------------------------------------------------
print("\nCola A\tCola B\tCola Resultado")
for i in range(n):
    print(f"{cola_a[i]:>5}\t{cola_b[i]:>5}\t{cola_c[i]:>8}")
