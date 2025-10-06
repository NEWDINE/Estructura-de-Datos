class Pila:
    def __init__(self, nombre):
        self.nombre = nombre
        self._datos = []

    def push(self, x):
        self._datos.append(x)

    def pop(self):
        return self._datos.pop()

    def top(self):
        return self._datos[-1] if self._datos else None

    def __len__(self):
        return len(self._datos)

    def __repr__(self):
        return f"{self.nombre}:{self._datos}"

def dibujar(A, B, C, N=3):
    torres = [A._datos[:], B._datos[:], C._datos[:]]
    for i in range(N-1, -1, -1):
        fila = []
        for t in torres:
            if len(t) > i:
                disco = t[i]
                fila.append(f"{disco:^5}")
            else:
                fila.append("  |  ")
        print("   ".join(fila))
    print("  A     B     C  ")
    print()

def mover(origen: Pila, destino: Pila):
    if len(origen) == 0:
        print("✗ Movimiento inválido: torre de origen vacía.")
        return False
    d = origen.top()
    if destino.top() is not None and destino.top() < d:
        print(f"✗ Movimiento inválido: no puedes poner {d} sobre {destino.top()}.")
        return False
    destino.push(origen.pop())
    return True

def resuelto(B: Pila, N: int) -> bool:
    return len(B) == N and B._datos == sorted(B._datos)

def main():
    N = 3
    A, B, C = Pila("A"), Pila("B"), Pila("C")
    for disco in range(N, 0, -1):
        A.push(disco)

    print("=== TORRES DE HANOI (3 discos) — Modo interactivo ===")
    print("Mueve tú: escribe jugadas como 'A B' (de A a B). Comandos: 'help', 'q' para salir.\n")
    dibujar(A, B, C, N)

    nombre_a_pila = {"A": A, "B": B, "C": C}
    movimientos = 0
    minimo = 2**N - 1

    while True:
        cmd = input("Movimiento (ej. 'A B'): ").strip().upper()
        if cmd in ("Q", "QUIT", "SALIR"):
            print("Saliendo…")
            break
        if cmd in ("H", "HELP", "?"):
            print("Formato: <origen> <destino>  con origen/destino en {A, B, C}. Ejemplo:  A B")
            print("Regla: no puedes poner un disco grande sobre uno pequeño.\n")
            continue

        partes = cmd.split()
        if len(partes) != 2 or partes[0] not in nombre_a_pila or partes[1] not in nombre_a_pila:
            print("✗ Entrada inválida. Usa algo como:  A B\n")
            continue

        o, d = nombre_a_pila[partes[0]], nombre_a_pila[partes[1]]
        if o is d:
            print("✗ Origen y destino no pueden ser iguales.\n")
            continue

        if mover(o, d):
            movimientos += 1
            dibujar(A, B, C, N)
            if resuelto(B, N):
                print(f"¡Felicidades! Resuelto en {movimientos} movimientos. Óptimo: {minimo}.")
                break

if __name__ == "__main__":
    main()
