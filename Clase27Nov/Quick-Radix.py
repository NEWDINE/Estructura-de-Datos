import random
import sys

# aumentar límite de recursión para evitar errores con QuickSort en listas grandes
sys.setrecursionlimit(20000)

# ================================
#     QUICKSORT – PASO A PASO
# ================================
def quicksort(lista):
    pasos = 0
    history = []

    def qs(arr, low, high):
        nonlocal pasos
        if low < high:
            p = partition(arr, low, high)
            qs(arr, low, p - 1)
            qs(arr, p + 1, high)

    def partition(arr, low, high):
        nonlocal pasos
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            pasos += 1
            history.append(f"Comparando {arr[j]} con pivot {pivot}")
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                history.append(f"Intercambio → {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        history.append(f"Pivot colocado → {arr}")
        return i + 1

    a = lista.copy()
    qs(a, 0, len(a) - 1)

    return a, pasos, history


# ================================
#       RADIX SORT – PASO A PASO
# ================================
def radix_sort(lista):
    pasos = 0
    history = []

    a = lista.copy()
    max_num = max(a)
    exp = 1

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in a:
            pasos += 1
            digit = (num // exp) % 10
            history.append(f"Número {num} → dígito {digit}")
            buckets[digit].append(num)

        a = [num for bucket in buckets for num in bucket]
        history.append(f"Después de ordenar por dígito {exp}: {a}")
        exp *= 10

    return a, pasos, history


# ================================
#     PROGRAMA PRINCIPAL
# ================================

# Generar la lista aleatoria de 1000 números
lista = [random.randint(0, 9999) for _ in range(1000)]

print("Lista generada automáticamente con 1000 números aleatorios.\n")

# QUICK
orden_qs, pasos_qs, hist_qs = quicksort(lista)

# RADIX
orden_rs, pasos_rs, hist_rs = radix_sort(lista)

# === IMPRIMIR TODO EL PASO A PASO (SIN CONDICIÓN) ===
print("\n========= QUICK SORT PASO A PASO (COMPLETO) =========")
for h in hist_qs:
    print(h)

print("\n========= RADIX SORT PASO A PASO (COMPLETO) =========")
for h in hist_rs:
    print(h)

# Resultados finales
print("\n==========================================")
print("RESULTADOS FINALES")
print("QuickSort pasos:", pasos_qs)
print("RadixSort pasos:", pasos_rs)

print("\nMEJOR ALGORITMO:")

if pasos_qs < pasos_rs:
    print("➡️ QuickSort fue el más eficiente.")
elif pasos_rs < pasos_qs:
    print("➡️ Radix Sort fue el más eficiente.")
else:
    print("➡️ Empate (ambos usaron la misma cantidad de pasos).")
