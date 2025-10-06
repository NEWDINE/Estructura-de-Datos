class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.datos = []

    @property
    def tope(self):
        return len(self.datos)

    def push(self, x):
        if self.tope >= self.capacidad:
            return "OVERFLOW"
        self.datos.append(x)
        return "OK"

    def pop(self, nombre_var):
        if self.tope == 0:
            return "UNDERFLOW"
        valor = self.datos.pop()
        return f"{nombre_var}={valor}"

def mostrar(paso, operacion, resultado, pila):
    contenido = "[" + ", ".join(pila.datos) + "]" if pila.datos else "[]"
    print(f"{paso:>2} | {operacion:<24} | {resultado:<14} | TOPE={pila.tope:<2} | {contenido}")
    print("   " + " " * 58 + (f"↑ cima = {pila.datos[-1]}" if pila.datos else "↑ pila vacía"))

print(" # | Operación                | Resultado      | TOPE | Pila (abajo→arriba)")

p = Pila(8)
mostrar("–", "Inicio", "-", p)

pasos = [
    ("a", ("Insertar(X)", lambda: p.push("X"))),
    ("b", ("Insertar(Y)", lambda: p.push("Y"))),
    ("c", ("Eliminar(Z)", lambda: p.pop("Z"))),
    ("d", ("Eliminar(T)", lambda: p.pop("T"))),
    ("e", ("Eliminar(U)", lambda: p.pop("U"))),
    ("f", ("Insertar(V)", lambda: p.push("V"))),
    ("g", ("Insertar(W)", lambda: p.push("W"))),
    ("h", ("Eliminar(p)", lambda: p.pop("p"))),
    ("i", ("Insertar(R)", lambda: p.push("R"))),
]

for paso, (op, accion) in pasos:
    res = accion()
    mostrar(paso, op, res, p)

print("\nFinal:", p.datos, "— TOPE =", p.tope)
